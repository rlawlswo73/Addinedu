import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

# ui
from_class = uic.loadUiType("Test.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Test, PyQt!!")
        self.textEdit.setText("This is text editor.")

        self.pushButton_1.clicked.connect(self.button1_Clicked)
        self.pushButton_2.clicked.connect(self.button2_Clicked)
        self.pushButton_3.clicked.connect(self.button3_Clicked)

        # self.radio_1.clicked.connect(self.radio1_Clicked)
        # self.radio_2.clicked.connect(self.radio2_Clicked)
        # self.radio_3.clicked.connect(self.radio3_Clicked)

        self.radio_1.clicked.connect(self.radioClicked)
        self.radio_2.clicked.connect(self.radioClicked)
        self.radio_3.clicked.connect(self.radioClicked)
        
        self.checkBox_1.clicked.connect(self.check1_clicked)
        self.checkBox_2.clicked.connect(self.check2_clicked)
        self.checkBox_3.clicked.connect(self.check3_clicked)
        self.checkBox_4.clicked.connect(self.check4_clicked)

    def button1_Clicked(self):
        self.textEdit.setText("Button_1")
        self.radio_1.setChecked(True)

    def button2_Clicked(self):
        self.textEdit.setText("Button_2")
        self.radio_2.setChecked(True)

    def button3_Clicked(self):
        self.textEdit.setText("Button_3")
        self.radio_3.setChecked(True)

    # def radio1_Clicked(self):
    #     self.textEdit.setText("Radio_1")

    # def radio2_Clicked(self):
    #     self.textEdit.setText("Radio_2")

    # def radio3_Clicked(self):
    #     self.textEdit.setText("Radio_3")

    def radioClicked(self):
        if self.radio_1.isChecked():
            self.textEdit.setText("Radio_1")

        elif self.radio_2.isChecked():
            self.textEdit.setText("Radio_2")

        elif self.radio_3.isChecked():
            self.textEdit.setText("Radio_3")

        else :
            self.textEdit.setText("Unkonwn")

    def check1_clicked(self):
        if (self.checkBox_1.isChecked()):
            self.textEdit.setText("CheckBox_1 Checked")
            self.checkBox_5.setChecked(True)
        else :
            self.textEdit.setText("CheckBox_1 Unchecked")
            self.checkBox_5.setChecked(False)

    def check2_clicked(self):
        if (self.checkBox_2.isChecked()):
            self.textEdit.setText("CheckBox_2 Checked")
            self.checkBox_6.setChecked(True)
        else :
            self.textEdit.setText("CheckBox_2 Unchecked")
            self.checkBox_6.setChecked(False)

    def check3_clicked(self):
        if (self.checkBox_3.isChecked()):
            self.textEdit.setText("CheckBox_3 Checked")
            self.checkBox_7.setChecked(True)
        else :
            self.textEdit.setText("CheckBox_3 Unchecked")
            self.checkBox_7.setChecked(False)

    def check4_clicked(self):
        if (self.checkBox_4.isChecked()):
            self.textEdit.setText("CheckBox_4 Checked")
            self.checkBox_8.setChecked(True)
        else :
            self.textEdit.setText("CheckBox_4 Unchecked")
            self.checkBox_8.setChecked(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec())