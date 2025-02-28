import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QLine, QPoint
import cv2
import imutils
import urllib.request

from_class = uic.loadUiType("opencv.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pixmap = QPixmap()

        self.btnOpen.clicked.connect(self.openFile)

    def openFile(self):
        file = QFileDialog.getOpenFileName(self, filter='Image (*.*)')

        image = cv2.imread(file[0])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  

        h, w, c = image.shape
        qimage = QImage(image.data, w, h, w*c, QImage.Format_RGB888)

        self.pixmap = self.pixmap.fromImage(qimage)
        self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

        self.label.setPixmap(self.pixmap)

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())