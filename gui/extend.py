from PyQt5 import QtCore

from gui.model import Ui_MainWindow
from gui.pandasModel import PandasModel


class extendedMainWindow(Ui_MainWindow):

    def __init__(self, mainWindow):
        self.setupUi(mainWindow)

    def setData(self, data):
        model = PandasModel(data)
        self.cryptedPswView.setModel(model)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Password"))
        self.insertDataButton.setText(_translate("MainWindow", "Invia"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Aggiungi password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Genera password"))