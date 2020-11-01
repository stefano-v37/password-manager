from PyQt5 import QtCore
from pandas import DataFrame

from PasswordManager import get_configuration, Instance
from gui.model import Ui_MainWindow
from gui.pandasModel import PandasModel

from datetime import datetime as dt


class extendedMainWindow(Ui_MainWindow):

    def __init__(self, mainWindow, instance):
        self.setupUi(mainWindow)
        self.users = get_configuration()['output_path']
        self.__extend__()
        self.setUser(instance)

    def setUser(self, init):
        if isinstance(init, Instance):
            self.instance = init
        elif isinstance(init, str):
            self.instance = Instance(user=init)
        else:
            print("provide a proper initialization")
        self.refresh()

    def changeUser(self):
        print("current user is: " + self.userList.currentText())
        self.setUser(self.userList.currentText())

    def insertdataclick(self):
        self.instance.add_data(date=dt.now(),
                               provider=self.inputProvider.text(),
                               user=self.inputUsr.text(),
                               psw=self.inputPsw.text(),
                               key_generator_phrase=self.inputKey.text(),
                               iv_generator_phrase=self.inputIv.text())
        self.refresh()

    def deletedataclick(self):
        input = self.deleteRowInput.text()
        if ", " in input:
            rows = input.split(", ")
            rows = [int(x) for x in rows]
        if "," in input:
            rows = input.split(",")
            rows = [int(x) for x in rows]
        else:
            rows = int(input)
        self.instance.delete_row(rows)
        self.refresh()

    def decryptdataclick(self):
        self.refresh()
        temp = self.instance.get_all_df(self.lineEditSendKey.text(), self.lineEditSendIv.text())
        self.refresh(temp)

    def refresh(self, data=None):
        self.setData(data)
        self.refreshUser()

    def refreshUser(self):
        _translate = QtCore.QCoreApplication.translate
        self.path.setText(_translate("MainWindow", self.instance.link))
        self.userList.setCurrentIndex(list(self.users).index(self.instance.user))

        try:
            self.disconnectActions()
            self.connectActions()

        except TypeError as te:
            print(te)
            self.connectActions()

    def disconnectActions(self):
        self.userList.disconnect()
        self.insertDataButton.disconnect()
        self.pushButtonDeleteRow.disconnect()
        self.pushButtonSaveData.disconnect()
        self.pushButtonDecrypt.disconnect()

    def connectActions(self):
        self.userList.activated.connect(self.changeUser)
        self.insertDataButton.clicked.connect(self.insertdataclick)
        self.pushButtonDeleteRow.clicked.connect(self.deletedataclick)
        self.pushButtonSaveData.clicked.connect(self.instance.save_df)
        self.pushButtonDecrypt.clicked.connect(self.decryptdataclick)

    def setData(self, data=None):
        if type(data) == DataFrame:
            model = PandasModel(data)
        else:
            model = PandasModel(self.instance.data)
        self.tabWidget.setCurrentIndex(0)
        self.cryptedPswView.setModel(model)

    def __extend__(self):
        _translate = QtCore.QCoreApplication.translate

        # tab0
        self.userList.addItems(self.users.keys())

        # ! tab 1
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Password"))
        self.insertDataButton.setText(_translate("MainWindow", "Send"))

        # !! tab2
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Add password"))

        # !!! tab3
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Generate password"))
