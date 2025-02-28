import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import uic

# ui
from_class = uic.loadUiType("Calculator.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Calculator, PyQt!!")

        # visual
        self.value.setText("0")
        self.value.setStyleSheet('color:white;')
        self.value.setAlignment(Qt.AlignRight)
        self.formula.setText("")
        self.formula.setStyleSheet('color:white;')
        self.point.setStyleSheet('color:white; background-color:rgb(40, 40, 40); border-radius: 35px;')
        self.number_0.setStyleSheet('color:white; background-color:rgb(40, 40, 40); border-radius: 35px; text-align: left; padding-left: 28px;')
        self.number_1.setStyleSheet('color:white; background-color:rgb(40, 40, 40); border-radius: 35px;')
        self.number_2.setStyleSheet('color:white; background-color:rgb(40, 40, 40); border-radius: 35px;')
        self.number_3.setStyleSheet('color:white; background-color:rgb(40, 40, 40); border-radius: 35px;')
        self.number_4.setStyleSheet('color:white; background-color:rgb(40, 40, 40); border-radius: 35px;')
        self.number_5.setStyleSheet('color:white; background-color:rgb(40, 40, 40); border-radius: 35px;')
        self.number_6.setStyleSheet('color:white; background-color:rgb(40, 40, 40); border-radius: 35px;')
        self.number_7.setStyleSheet('color:white; background-color:rgb(40, 40, 40); border-radius: 35px;')
        self.number_8.setStyleSheet('color:white; background-color:rgb(40, 40, 40); border-radius: 35px;')
        self.number_9.setStyleSheet('color:white; background-color:rgb(40, 40, 40); border-radius: 35px;')

        self.point.setStyleSheet('color:white; background-color:rgb(252, 120, 04); border-radius: 35px;')

        self.plus.setStyleSheet('color:white; background-color:rgb(252, 120, 04); border-radius: 35px;')
        self.minus.setStyleSheet('color:white; background-color:rgb(252, 120, 04); border-radius: 35px;')
        self.mul.setStyleSheet('color:white; background-color:rgb(252, 120, 04); border-radius: 35px;')
        self.div.setStyleSheet('color:white; background-color:rgb(252, 120, 04); border-radius: 35px;')

        self.power.setStyleSheet('color:black; background-color:rgb(150, 150, 150); border-radius: 35px;')
        self.ch_sign.setStyleSheet('color:black; background-color:rgb(150, 150, 150); border-radius: 35px;')
        self.delet.setText("C")
        self.delet.setStyleSheet('color:black; background-color:rgb(150, 150, 150); border-radius: 35px;')

        self.cal.setStyleSheet('color:white; background-color:rgb(252, 120, 04); border-radius: 35px;')

        # operator 연산자
        # operand_1
        # operand_2
        self.oper()
        self.pmmd()
        self.result = 0
        self.background_formula = ""

        # input
        # number
        self.number_0.clicked.connect(self.clicked_0)
        self.number_1.clicked.connect(self.clicked_1)
        self.number_2.clicked.connect(self.clicked_2)
        self.number_3.clicked.connect(self.clicked_3)
        self.number_4.clicked.connect(self.clicked_4)
        self.number_5.clicked.connect(self.clicked_5)
        self.number_6.clicked.connect(self.clicked_6)
        self.number_7.clicked.connect(self.clicked_7)
        self.number_8.clicked.connect(self.clicked_8)
        self.number_9.clicked.connect(self.clicked_9)
        # point
        self.point.clicked.connect(self.clicked_point)
        # power
        self.power.clicked.connect(self.clicked_power)
        # change_sign
        self.ch_sign.clicked.connect(self.clicked_ch_sign)
        # delete
        self.delet.clicked.connect(self.clicked_delet)
        # operator
        self.plus.clicked.connect(self.clicked_plus)
        self.minus.clicked.connect(self.clicked_minus)
        self.mul.clicked.connect(self.clicked_mul)
        self.div.clicked.connect(self.clicked_div)
        # calculate
        self.cal.clicked.connect(self.clicked_cal)

    # function
    def pmmd(self):
        self.tmp_number = 0
        self.weight = 10
        self.dec = 1
        self.flag = 1
        self.sign = 1

    def oper(self):
        self.operator = ""
        self.operand_1 = 0
        self.operand_2 = 0

    def clicked_0(self):
        self.delet.setText("C")
        self.tmp_number *= float(self.weight)

        self.tmp_number = float(self.tmp_number) + float(0 * self.dec * int(self.sign))
        self.value.setText(str(self.print_round(self.tmp_number)))
        if self.flag == 0:
            self.dec *= 0.1
    def clicked_1(self):
        self.delet.setText("C")
        self.tmp_number *= float(self.weight)
        self.tmp_number = float(self.tmp_number) + float(1 * self.dec * int(self.sign))
        self.value.setText(str(self.print_round(self.tmp_number)))
        if self.flag == 0:
            self.dec *= 0.1
    def clicked_2(self):
        self.delet.setText("C")
        self.tmp_number *= float(self.weight)
        self.tmp_number = float(self.tmp_number) + float(2 * self.dec * int(self.sign))
        self.value.setText(str(self.print_round(self.tmp_number)))
        if self.flag == 0:
            self.dec *= 0.1
    def clicked_3(self):
        self.delet.setText("C")
        self.tmp_number *= float(self.weight)
        self.tmp_number = float(self.tmp_number) + float(3 * self.dec * int(self.sign))
        self.value.setText(str(self.print_round(self.tmp_number)))
        if self.flag == 0:
            self.dec *= 0.1
    def clicked_4(self):
        self.delet.setText("C")
        self.tmp_number *= float(self.weight)
        self.tmp_number = float(self.tmp_number) + float(4 * self.dec * int(self.sign))
        self.value.setText(str(self.print_round(self.tmp_number)))
        if self.flag == 0:
            self.dec *= 0.1
    def clicked_5(self):
        self.delet.setText("C")
        self.tmp_number *= float(self.weight)
        self.tmp_number = float(self.tmp_number) + float(5 * self.dec * int(self.sign))
        self.value.setText(str(self.print_round(self.tmp_number)))
        if self.flag == 0:
            self.dec *= 0.1
    def clicked_6(self):
        self.delet.setText("C")
        self.tmp_number *= float(self.weight)
        self.tmp_number = float(self.tmp_number) + float(6 * self.dec * int(self.sign))
        self.value.setText(str(self.print_round(self.tmp_number)))
        if self.flag == 0:
            self.dec *= 0.1
    def clicked_7(self):
        self.delet.setText("C")
        self.tmp_number *= float(self.weight)
        self.tmp_number = float(self.tmp_number) + float(7 * self.dec * int(self.sign))
        self.value.setText(str(self.print_round(self.tmp_number)))
        if self.flag == 0:
            self.dec *= 0.1
    def clicked_8(self):
        self.delet.setText("C")
        self.tmp_number *= float(self.weight)
        self.tmp_number = float(self.tmp_number) + float(8 * self.dec * int(self.sign))
        self.value.setText(str(self.print_round(self.tmp_number)))
        if self.flag == 0:
            self.dec *= 0.1
    def clicked_9(self):
        self.delet.setText("C")
        self.tmp_number *= float(self.weight)
        self.tmp_number = float(self.tmp_number)+ float(9 * self.dec * int(self.sign))
        self.value.setText(str(self.print_round(self.tmp_number)))
        if self.flag == 0:
            self.dec *= 0.1

    def clicked_point(self):
        self.delet.setText("C")
        self.value.setText(str(self.print_round(self.tmp_number))+".")
        tmp_str = str(self.tmp_number)
        self.tmp_number = float(tmp_str[:tmp_str.rfind('.')])
        self.weight = 1
        self.dec = 0.1
        self.flag = 0

    def clicked_power(self):
        self.tmp_number = float(pow(self.tmp_number, 2))
        self.value.setText(str(self.print_round(self.tmp_number)))

    def clicked_ch_sign(self):
        self.tmp_number *= -1
        self.sign *= -1
        
        if str(self.tmp_number) == '0' or str(self.tmp_number) == '':
            self.value.setText('-')
        else: 
            self.value.setText(str(self.print_round(self.tmp_number)))

    def clicked_delet(self):
        self.tmp_number *= 1
        temp = str(self.print_round(self.tmp_number))
        if len(temp) > 1:
            if len(temp) >= 2 and temp[-2] == "." and temp[-1] == "0":
                self.weight = 10
                self.dec = 1
                self.flag = 1
                self.tmp_number = int(temp[:-2])
            else :
                self.tmp_number = temp[:-1] * 1
                self.dec *= 10
                if temp == "":
                    self.delet.setText("AC")
            self.value.setText(str(self.print_round(self.tmp_number)))
            self.tmp_number *= 1
        else :
            self.delet.setText("AC")
            self.result = 0
            self.oper()
            self.pmmd()
            self.background_formula = ""
            self.value.setText("0")
            self.formula.setText("")

        float_string = str(self.print_round(self.tmp_number))
        float_digit = 1
        
        if float_string.rfind(".") != -1:
            float_digit = len(float_string) - float_string.rfind(".")
            self.dec = pow(0.1, float_digit)
        
        self.tmp_number *= 1

    def clicked_plus(self):
        if int(self.tmp_number) == 0:
            self.operator = "+"
        else :
            self.operand_1 = self.tmp_number
            self.operator = "+"
            self.pmmd()
        self.formula.setText(str(self.print_round(self.operand_1))+" "+"+")
    def clicked_minus(self):
        if int(self.tmp_number) == 0:
            self.operator = "-"
        else :
            self.operand_1 = self.tmp_number
            self.operator = "-"
            self.pmmd()
        self.formula.setText(str(self.print_round(self.operand_1))+" "+"-")
    def clicked_mul(self):
        if int(self.tmp_number) == 0:
            self.operator = "x"
        else :
            self.operand_1 = self.tmp_number
            self.operator = "x"
            self.pmmd()
        self.formula.setText(str(self.print_round(self.operand_1))+" "+"x")
    def clicked_div(self):
        if int(self.tmp_number) == 0:
            self.operator = "/"
        else :
            self.operand_1 = self.tmp_number
            self.operator = "/"
            self.pmmd()
        self.formula.setText(str(self.print_round(self.operand_1))+" "+"/")

    def clicked_cal(self):
        self.operand_2 = self.tmp_number
        if self.operand_1 != 0 and self.operand_2 != 0:
            if self.operator == "+":
                self.result = float(self.operand_1) + float(self.operand_2)
            elif self.operator == "-":
                self.result = float(self.operand_1) - float(self.operand_2)
            elif self.operator == "x":
                self.result = float(self.operand_1) * float(self.operand_2)
            elif self.operator == "/":
                self.result = float(self.operand_1) / float(self.operand_2)

        self.formula.setText(str(self.print_round(self.operand_1))+" "+self.operator+" "+str(self.print_round(self.operand_2)))
        self.value.setText(str(self.print_round(self.result)))
        self.delet.setText("C")

        self.oper()
        self.sign = 1
        self.tmp_number = self.result * 1
        
        float_string = str(self.print_round(self.tmp_number))
        float_digit = 1

        if float_string.rfind(".") != -1:
            float_digit = len(float_string) - float_string.rfind(".") - 1
            self.result = 0
            self.weight = 1
            self.dec = pow(0.1, float_digit)
            self.flag = 0
        else :
            float_digit = 1
            self.pmmd()

    def print_round(self, x):
        if x != '' and x != "-":
            x_str = str(float(x))
            find = x_str.rfind('.')
            integer = int(x_str[:find])
            decimal = float(x_str[find:])

            if decimal == 0.0:
                return int(integer)
            else : 
                return round(float(x), 9)
        else:
            return ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec())