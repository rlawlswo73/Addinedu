import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import urllib.request
from PyQt5.QtCore import Qt

from_class = uic.loadUiType("Test9.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.spinBox.setRange(1, 100)

        min = self.spinBox.minimum()
        max = self.spinBox.maximum()
        step = self.spinBox.singleStep() 
        self.spinBox.setValue(max)
        
        self.editMin.setText(str(min))
        self.editMax.setText(str(max))
        self.editStep.setText(str(step))

        self.slider.setRange(min, max)
        self.slider.setSingleStep(step)
        self.slider.setValue(max)

        self.labelPixmap.setAlignment(Qt.AlignLeft)

        self.btnApply.clicked.connect(self.apply)
        self.spinBox.valueChanged.connect(self.changeSpinBox)
        self.slider.valueChanged.connect(self.changeSlider)

        self.url = 'https://imageio.forbes.com/specials-images/imageserve/61b1fb3e8d51f2303254ff62/A-funny-cat-sits-like-a-person-/960x0.jpg?format=jpg&width=1440'
        self.image = urllib.request.urlopen(self.url).read()

        self.pixmap = QPixmap()
        # self.pixmap.load('../data/cat.png')
        self.pixmap.loadFromData(self.image)

        self.pixmap = self.pixmap.scaled(self.labelPixmap.width(), self.labelPixmap.height())
        self.labelPixmap.setPixmap(self.pixmap)

        # self.labelPixmap.setPixmap(self.pixmap)
        # self.labelPixmap.resize(self.pixmap.width(), self.pixmap.height())

        self.btnRead.clicked.connect(self.openImage)
        self.btnSave.clicked.connect(self.saveImage)

    def saveImage(self):
        name = QFileDialog.getSaveFileName(self, 'Save Image', '../data/', 'Image File(*.png *.jpg *.webp)')
        print(name[0])
        self.pixmap.save(str(name[0]))
        QMessageBox.warning(self, 'Saved', 'Image has save')

    def openImage(self):
        name = QFileDialog.getOpenFileName(self, 'Open Image', '../data/', 'Image File(*.png *.jpg *.webp)')

        print("--- " + str(name[0]) + " ---")
        if name[0]:
            self.url = str(name[0])

            self.pixmap.load(self.url)

            self.pixmap = self.pixmap.scaled(self.labelPixmap.width(), self.labelPixmap.height())
            self.labelPixmap.setPixmap(self.pixmap)

            self.labelPixmap.setPixmap(self.pixmap)
            self.labelPixmap.resize(self.pixmap.width(), self.pixmap.height())

    def changeSlider(self):
        actualValue = self.slider.value()
        self.labelValue2.setText(str(actualValue))
        self.spinBox.setValue(actualValue)
        self.changeImage(actualValue)

    def changeSpinBox(self):
        actualValue = self.spinBox.value()
        self.labelValue.setText(str(actualValue))
        self.slider.setValue(actualValue)
        self.changeImage(actualValue)

    def changeImage(self, actualValue):
        self.pixmap.loadFromData(self.image)
        self.pixmap = self.pixmap.scaled(int(self.labelPixmap.width() * (actualValue / 100)), int(self.labelPixmap.height() * (actualValue / 100)))
        self.labelPixmap.setPixmap(self.pixmap)

    def apply(self):
        min = self.editMin.text()
        max = self.editMax.text()
        step = self.editStep.text()

        self.spinBox.setRange(int(min), int(max))
        self.spinBox.setSingleStep(int(step))
        
        self.slider.setRange(int(min), int(max))
        self.slider.setSingleStep(int(step))

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())