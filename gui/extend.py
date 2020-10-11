import pandas
from PyQt5 import QtCore
from pandas import DataFrame

from gui.model import Ui_MainWindow
from gui.pandasModel import PandasModel

from datetime import datetime as dt


class extendedMainWindow(Ui_MainWindow):

    def __init__(self, mainWindow, instance):
        self.setupUi(mainWindow)
        self.__extend__()
        self.instance = instance
        self.setData()

        self.insertDataButton.clicked.connect(self.insertdataclick)
        self.pushButtonDeleteRow.clicked.connect(self.deletedataclick)
        self.pushButtonSaveData.clicked.connect(self.instance.save_df)
        self.pushButtonDecrypt.clicked.connect(self.decryptdataclick)

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

    def refresh(self, data = None):
        self.setData(data)

    def setData(self, data=None):
        if type(data) == DataFrame:
            print('ok')
            model = PandasModel(data)
        else:
            model = PandasModel(self.instance.data)
        self.tabWidget.setCurrentIndex(0)
        self.cryptedPswView.setModel(model)


    def __extend__(self):
        _translate = QtCore.QCoreApplication.translate

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Password"))
        self.insertDataButton.setText(_translate("MainWindow", "Invia"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Aggiungi password"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Genera password"))
