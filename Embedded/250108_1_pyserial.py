import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import serial
import struct

from_class = uic.loadUiType("/home/kjj73/dev_ws/Embedded/250108_0_pyserial.ui")[0]
class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.uid = bytes(4)
        self.conn = serial.Serial(port="/dev/ttyACM0", baudrate=9600, timeout=1)

        self.recv = Receiver(self.conn) 
        self.recv.start()

        self.resetButton.clicked.connect(self.reset)
        self.chargeButton.clicked.connect(self.charge)
        self.paymentButton.clicked.connect(self.payment)

        self.disable()

        self.timer = QTimer()
        self.timer.setInterval(3000)
        self.timer.timeout.connect(self.getStatus)
        self.timer.start()

        self.recv.detected.connect(self.detected)
        self.recv.recvTotal.connect(self.recvTotal)
        self.recv.changedTotal.connect(self.changedTotal)
        self.recv.noCard.connect(self.noCard)

    def enable(self, total):
        self.totalLabel.setText(str(total))
        self.chargeEdit.setDisabled(False)
        self.chargeButton.setDisabled(False)
        self.paymentEdit.setDisabled(False)
        self.paymentButton.setDisabled(False)

    def disable(self):
        self.totalLabel.setText("-")
        self.chargeEdit.setDisabled(True)
        self.chargeButton.setDisabled(True)
        self.paymentEdit.setDisabled(True)
        self.paymentButton.setDisabled(True)

    def send(self, command, data = 0):
        print("send")
        req_data = struct.pack('<2s4sic', command, self.uid, data, b'\n')
        self.conn.write(req_data)
        return

    def getStatus(self):
        print("getStatus")
        self.send(b'GS')
        return
    
    def detected(self, uid):
        print("detected")
        self.uid = uid 
        self.timer.stop()
        # self.enable(0)

        self.getTotal()
        self.resetButton.setDisabled(False)
        return
    
    def noCard(self):
        print("noCard")
        if(self.timer.isActive() == False):
            print("startTimer")
            self.timer.start()
        
        self.disable()
        return
    
    def getTotal(self):
        print("getTotal")
        self.send(b'GT')
        return

    def recvTotal(self, total):
        print("recvTotal")
        self.enable(total)
        self.chargeEdit.setText("")
        self.paymentEdit.setText("")

    def setTotal(self, total):
        print("setTotal")
        self.send(b'ST', total)
        return

    def changedTotal(self):
        self.getTotal()
        return

    def reset(self):
        print("reset")
        self.setTotal(0)
        return
    
    def charge(self):
        print("charge")
        total = int(self.totalLabel.text())
        charge = int(self.chargeEdit.text())
        self.setTotal(total + charge)
        return
    
    def payment(self):
        print("payment")
        total = int(self.totalLabel.text())
        payment = int(self.paymentEdit.text())

        if(total < payment):
            QMessageBox.warning(self, 'Arduino Manager', '잔액이 부족합니다.')
            self.paymentEdit.setText("")
        else :
            total = total - payment
            self.setTotal(total)

        return
    
class Receiver(QThread):
    detected = pyqtSignal(bytes)
    recvTotal = pyqtSignal(int)
    changedTotal = pyqtSignal()
    noCard = pyqtSignal()

    def __init__(self, conn, parent=None):
        super(Receiver, self).__init__(parent)
        self.is_running = False 
        self.conn = conn 
        print("recv init")
    
    def run(self):
        print("recv start")
        self.is_running = True
        while(self.is_running == True):     
            if self.conn.readable():
                res = self.conn.read_until(b'\n')
                # print(res)
                if len(res) > 0:
                    res = res[:-2]
                    cmd = res[:2].decode()
                    if cmd == 'GS' and res[2] == 0:
                        print("recv detected")
                        self.detected.emit(res[3:])
                    elif cmd == 'GT' and res[2] == 0:
                        print("recvTotal")
                        print(len(res))
                        self.recvTotal.emit(int.from_bytes(res[3:7], 'little'))
                    elif cmd == 'ST' and res[2] == 0:
                        print("setTotal")
                        self.changedTotal.emit()
                    elif res[2].to_bytes(1, 'little') == b'\xfa':
                        print("recv noCard")
                        self.noCard.emit()
                    else :
                        print("unknown error")
                        print(cmd)
    
    def stop(self):
        print("recv stop")
        self.is_running = False
    
if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())