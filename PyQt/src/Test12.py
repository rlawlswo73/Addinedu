import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QLine, QPoint
import urllib.request

from_class = uic.loadUiType("/home/kjj73/dev_ws/PyQt/src/Test12.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pixmap = QPixmap(self.label.width(), self.label.height())
        self.pixmap.fill(Qt.white)

        self.label.setPixmap(self.pixmap)
        self.x, self.y = None, None

    def mouseMoveEvent(self, event):
        if self.x is None:
            self.x = event.x()
            self.y = event.y()
            return

        painter = QPainter(self.label.pixmap())
        # painter.setPen(QPen(Qt.blue, 5, Qt.SolidLine))
        painter.drawLine(self.x - self.label.x(), self.y - self.label.y(), event.x() - self.label.x(), event.y() - self.label.y())
        painter.end()
        self.update()

        self.x = event.x()
        self.y = event.y()

    def mouseReleaseEvent(self, event):
        self.x = None
        self.y = None


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())