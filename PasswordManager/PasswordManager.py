import os
import pandas as pd

from PasswordManager.utilities import crypt, uncrypt


class Instance:
    def __init__(self, path=None):
        if path:
            self.path = path
        else:
            this_dir = os.path.dirname(os.path.realpath(__file__))
            self.path = '\\'.join([str(x) for x in this_dir.split('\\')][:-1]) + '\\output'

        self.new = not 'password_list.csv' in os.listdir(self.path)
        self.link = self.path + '//' + 'password_list.csv'
        if self.new:
            self.data = pd.DataFrame(columns=['Date', 'Site/Provider', 'Username', 'Password'])
        else:
            self.data = pd.read_csv(self.link)
        self.data['Date'] = pd.to_datetime(self.data.Date)

    def add_data(self, date, provider, user, psw, key, **kwargs):
        success = False
        psw_crypted = crypt(psw, key)
        new_line = {'Date' : pd.to_datetime(date), 'Site/Provider' : provider, 'Username' : user, 'Password' : psw_crypted}
        check = self.check_duplicates(new_line)
        if check:
            if kwargs.pop('force_writing', False):
                self.data = self.data.append(new_line, ignore_index=True)
                success = True
        else:
            self.data = self.data.append(new_line, ignore_index=True)
            success = True
        if success:
            print(str(pd.DataFrame(self.data.iloc[-1])) + '\n' + 'has been written in the db, please save to store the data')

    def check_duplicates(self, new_line):
        check = [y for _,y in new_line.items()]
        line_counter = 0
        duplicates = []
        for x in self.data.values:
            flag = set(x) == set(check)
            if flag:
                duplicates.extend([line_counter])
            line_counter += 1
        if duplicates:
            print('Values already present in db, check below (use **kwargs to force the writing)')
            print(self.data.loc[self.data.index.isin(duplicates)])

        if duplicates:
            return True
        else:
            return False

    def save_db(self):
        self.data.to_csv(self.link, index = False)