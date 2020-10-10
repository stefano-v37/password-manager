from PyQt5 import QtWidgets

from PasswordManager import Instance
from gui.extend import extendedMainWindow
from gui.model import Ui_MainWindow
import sys

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = extendedMainWindow(MainWindow)

    instance = Instance()
    ui.setData(instance.data)


    MainWindow.show()
    sys.exit(app.exec_())