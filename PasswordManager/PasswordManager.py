import os
from datetime import datetime
import pandas as pd

from .utilities import crypt, uncrypt, get_configuration
from .utilities import THIS_DIR


class Instance:
    def __init__(self, path=None):
        path_std, columns_std, name_std = get_configuration()
        if path:
            if path == 'this':
                self.path = '\\'.join([str(x) for x in THIS_DIR.split('\\')][:-1]) + '\\output'
            else:
                self.path = path
        else:
            if path_std:
                self.path = os.environ.get(path_std)
            else:
                self.path = '\\'.join([str(x) for x in THIS_DIR.split('\\')][:-1]) + '\\output'

        self.new = not name_std in os.listdir(self.path)
        self.link = self.path + '//' + name_std
        if self.new:
            self.data = pd.DataFrame(columns=columns_std)
        else:
            self.data = pd.read_pickle(self.link)
        self.data['Date'] = pd.to_datetime(self.data.Date)
        self.update_df()

    def add_data(self, date, provider, user, psw, key_generator_phrase, **kwargs):
        success = False
        psw_crypted = crypt(psw, key_generator_phrase, kwargs.pop('iv_generator_phrase', None))
        new_line = {'Date' : pd.to_datetime(date), 'Site/Provider' : provider, 'Username' : user, 'Password' : psw_crypted}
        check = self.check_duplicates(new_line)
        if check:
            if kwargs.pop('force_writing', False):
                self.data = self.data.append(new_line, ignore_index=True)
                success = True
                force_flag = True
        else:
            self.data = self.data.append(new_line, ignore_index=True)
            success = True
            force_flag = False
        if success:
            self.update_df()
            if not force_flag:
                print(str(pd.DataFrame(self.data.iloc[-1])) + '\n' + 'has been written in the df, please save to store the data')

    def check_duplicates(self, new_line):
        check = [y for _,y in new_line.items() if _ != 'Password']
        line_counter = 0
        duplicates = []
        for x in self.data[[x for x in self.data.columns if x not in ['Password', 'Age']]].values:
            flag = set(x) == set(check)
            if flag:
                duplicates.extend([line_counter])
            line_counter += 1
        if duplicates:
            print('Values already present in df, check below (use **kwargs to force the writing)')
            print(self.data.loc[self.data.index.isin(duplicates)])

        if duplicates:
            return True
        else:
            return False

    def get_psw(self, provider, key_generator_phrase, iv_generator_phrase=None):
        selection = self.data.loc[self.data['Site/Provider'] == provider].copy()
        selection['Password'] = selection['Password'].apply(
            lambda row: uncrypt(row, key_generator_phrase, iv_generator_phrase))
        return selection

    def get_all_df(self, key_generator_phrase, iv_generator_phrase=None):
        temp = self.data.copy()
        for provider in self.data['Site/Provider'].unique():
            temp.loc[temp['Site/Provider'] == provider] = self.get_psw(provider, key_generator_phrase, iv_generator_phrase)
        return temp

    def update_df(self):
        self.data['Age'] = datetime.now() - self.data['Date']
        self.data['Age'] = self.data.Age.dt.days.astype(str) + ' ' + (self.data.Age.dt.days == 1).replace([True, False], ['day', 'days'])

    def save_df(self):
        self.data.to_pickle(self.link)