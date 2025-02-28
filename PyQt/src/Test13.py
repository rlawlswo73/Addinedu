import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import cv2, imutils
import time 
import datetime

from_class = uic.loadUiType("Test13.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.isCameraOn = False
        self.isRecStart = False
        self.btnRecord.hide()
        self.btnCapture.hide()

        self.pixmap = QPixmap()

        self.camera = Camera(self)
        self.camera.daemon = True

        self.record = Camera(self)
        self.record.daemon = True

        self.movie = Camera(self)
        self.movie.daemon = True

        self.btnOpen.clicked.connect(self.openFile)
        self.movie.update.connect(self.updateMovie)

        self.btnCamera.clicked.connect(self.clickCamera)
        self.camera.update.connect(self.updateCamera)
        self.btnRecord.clicked.connect(self.clickRecord)
        self.record.update.connect(self.updateRecording)
        self.btnCapture.clicked.connect(self.capture)

        self.count = 0

    def updateMovie(self):
        retval, self.frame = self.cap.read()
        if retval:
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)  

            h, w, c, = self.frame.shape
            self.qimage = QImage(self.frame.data, w, h, w*c, QImage.Format_RGB888)

            self.pixmap = self.pixmap.fromImage(self.qimage)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

            self.label.setPixmap(self.pixmap)
            # print(retval, self.frame)
        else :
            # print("over")
            self.cap.release()
            self.running = False

    def capture(self):
        self.now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = "../data/" + self.now + '.png'

        cv2.imwrite(filename, cv2.cvtColor(self.frame, cv2.COLOR_RGB2BGR))

    def clickRecord(self):
        if self.isRecStart == False:
            self.btnRecord.setText('Rec Stop')
            self.isRecStart = True

            self.recordingStart()
        else:
            self.btnRecord.setText('Rec Start')
            self.isRecStart = False

            self.recordingstop()

    def updateRecording(self):
        self.label_2.setText(str(self.count))
        self.writer.write(cv2.cvtColor(self.frame, cv2.COLOR_RGB2BGR))
        self.count += 1

    def recordingStart(self):
        self.record.running = True
        self.record.start()

        self.now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = "../data/" + self.now + ".avi"
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')

        w = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))

        self.writer = cv2.VideoWriter(filename , self.fourcc, 20.0, (w, h))

    def recordingstop(self):
        self.record.running = False

        if self.isRecStart == True:
            self.writer.release()

    def clickCamera(self):
        if self.isCameraOn == False:
            self.btnCamera.setText('Camera Off')
            self.isCameraOn = True
            self.btnRecord.show()
            self.btnCapture.show()

            self.cameraStart()
        else :
            self.btnCamera.setText('Camera On')
            self.isCameraOn = False
            self.btnRecord.hide()
            self.btnCapture.hide()

            self.cameraStop()
            self.recordingstop()

    def cameraStart(self):
        self.camera.running = True
        self.camera.start()
        self.video = cv2.VideoCapture(-1)

    def cameraStop(self):
        self.camera.running = False
        self.count = 0
        self.video.release()

        if self.isRecStart == True:
            self.writer.release()

    def openFile(self):
        self.file = QFileDialog.getOpenFileName(self, '', '../data/', filter='Image (*.*)')
        # print("@ @ @" + str(file[0]) +"@ @ @", str(file[0][-4:]))

        if self.file[0][-4:] == '.avi' or self.file[0][-4:] == '.mp4' or self.file[0][-4:] == '.mkv' or self.file[0][-4:] == '.mpg':
            self.movie.running = True
            self.movie.start()
            play_url = self.file[0]
            self.cap = cv2.VideoCapture(play_url)
            pass
        else:
            image = cv2.imread(file[0])
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            h, w, c = image.shape
            qimage = QImage(image.data, w, h, w*c, QImage.Format_RGB888)

            self.pixmap = self.pixmap.fromImage(qimage)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

            self.label.setPixmap(self.pixmap)

    def updateCamera(self):
        retval, self.frame = self.video.read()
        if retval:
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)  

            h, w, c, = self.frame.shape
            self.qimage = QImage(self.frame.data, w, h, w*c, QImage.Format_RGB888)

            self.pixmap = self.pixmap.fromImage(self.qimage)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

            self.label.setPixmap(self.pixmap)

        self.count += 1

class Camera(QThread):
    update = pyqtSignal()

    def __init__(self, sec=0, parent=None):
        super().__init__()
        self.main = parent
        self.running = True

    def run(self):
        count = 0
        while self.running == True:
            self.update.emit()
            time.sleep(0.1)
        
    def stop(self):
        self.running = False

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())