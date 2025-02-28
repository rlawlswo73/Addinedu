import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5 import uic
from PyQt5.QtCore import Qt
# from PyQt5.QtCore import QLine, QPoint
from PyQt5.QtCore import *
import urllib.request
import math


from_class = uic.loadUiType("practice.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.circle_size = 24

        self.pixmap = QPixmap(self.label.width(), self.label.height())
        self.pixmap.fill(Qt.white)

        self.label.setPixmap(self.pixmap)

        self.center_x, self.center_y = self.label.width() // 2, self.label.height() // 2
        self.start_x, self.end_x = 0, self.label.width()
        self.start_y, self.end_y = 0, self.label.height()

        self.position_x = 0
        self.position_y = int(self.circle_size * math.cos(self.position_x)) + self.center_y
        # print(center_x, center_y, start_x, end_x, start_y, end_y)

        painter = QPainter(self.label.pixmap())

        painter.setPen(QPen(Qt.black, 5, Qt.DotLine))
        painter.drawLine(self.start_x, self.center_y, self.end_x, self.center_y)

        painter.setPen(QPen(Qt.red, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
        painter.drawEllipse(self.start_x-(self.circle_size // 2), self.center_y-(self.circle_size // 2), self.circle_size, self.circle_size)

        timerVar = QTimer(self)
        timerVar.setInterval(75)
        timerVar.timeout.connect(self.draw)
        timerVar.start()
        print(timerVar.isActive(), "@!!!!!!!!!!")

    def draw(self):
        print(self.position_x, self.position_y)
        painter = QPainter(self.label.pixmap())
        painter.eraseRect(0, 0, self.end_x, self.end_y)

        painter.setPen(QPen(Qt.black, 5, Qt.DotLine))
        painter.drawLine(self.start_x, self.center_y, self.end_x, self.center_y)

        painter.setPen(QPen(Qt.yellow, 5, Qt.SolidLine))        
        painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
        painter.drawEllipse(int(self.position_x-(self.circle_size // 2)), int(self.position_y-(self.circle_size // 2)), self.circle_size, self.circle_size)
        
        if self.position_x >= self.end_x:
            self.position_x = 0
        else :
            self.position_x += 1
        self.position_y = int(150 * math.sin(self.position_x)) + self.center_y

        self.label.repaint()

        painter.end


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    # print("@!!!!!!!!!!#")

    sys.exit(app.exec_())