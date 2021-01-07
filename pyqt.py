from PyQt5 import QtWidgets, QtCore
# Импортируем наш файл
from weatherui import Ui_MainWindow
from weather import getWeather
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit.setStyleSheet('font-size: 20px; text-align: center')
        self.ui.label.setStyleSheet('font-size: 20px; text-align: center')

        self.ui.pushButton.setStyleSheet(
            "background-color: rgb(28, 43, 255);color: white; font-size: 20px;")
        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        self.ui.label.setText(getWeather(self.ui.lineEdit.text()))
        self.ui.label.adjustSize()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
