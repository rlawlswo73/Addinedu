import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QLine, QPoint
import urllib.request

from_class = uic.loadUiType("Test11.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pixmap = QPixmap(self.label.width(), self.label.height())
        self.pixmap.fill(Qt.white)

        self.label.setPixmap(self.pixmap)
        self.draw()

    def draw(self):
        painter = QPainter(self.label.pixmap())
        # painter.setPen(QPen(Qt.red, 20, Qt.SolidLine))
        # painter.drawPoint(100, 100)
        # painter.setPen(QPen(Qt.red, 5, Qt.SolidLine))
        # painter.setBrush(QBrush(Qt.black))
        # painter.drawRect(100, 100, 100, 100)
        # painter.drawEllipse(100, 100, 100, 100)

        painter.setPen(QPen(Qt.blue, 5, Qt.SolidLine))

        self.font = QFont()
        self.font.setFamily('Times')
        self.font.setBold(True)
        self.font.setPointSize(20)
        painter.setFont(self.font)

        painter.drawText(100, 100, 'This is drawText.')

        painter.end


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())