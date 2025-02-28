import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

# ui
from_class = uic.loadUiType("Test3.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Test3, PyQt!!")

        self.pushButton.clicked.connect(self.addText)
        self.pushButton_2.clicked.connect(self.clearText)
        self.lineEdit.returnPressed.connect(self.addText)

    def clearText(self):
        self.lineEdit.clear()
        self.textBrowser.clear()

    def addText(self):
        input = self.lineEdit.text()
        self.lineEdit.clear()
        self.textBrowser.append(input)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec())