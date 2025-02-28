import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import cv2, imutils
import time 
import datetime
import numpy as np

from_class = uic.loadUiType("Oneday_viewer.ui")[0]

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
        self.fileUpdate = Camera(self)
        self.fileUpdate.daemon = True

        self.btnFileOpen.clicked.connect(self.openFile)
        self.movie.update.connect(self.updateMovie)
        self.btnCamera.clicked.connect(self.clickCamera)
        self.camera.update.connect(self.updateCamera)
        self.btnRecord.clicked.connect(self.clickRecord)
        self.record.update.connect(self.updateRecording)
        self.btnCapture.clicked.connect(self.capture)
        self.fileUpdate.update.connect(self.fileUpdating)

        self.rbStream.clicked.connect(self.Stream_clicked)
        self.rbVideo.clicked.connect(self.Video_clicked)
        self.rbImage.clicked.connect(self.Image_clicked)

        self.optionStream.setGeometry(720, 170, 371, 541)
        self.optionStream.hide()
        self.optionVideo.setGeometry(720, 170, 371, 541)
        self.optionVideo.hide()
        self.optionImage.setGeometry(720, 170, 371, 541)
        self.optionImage.hide()

        self.recStat.setStyleSheet("Color : red")
        self.recStat.hide()
        self.record.running = False

        self.recCount = 0

        self.gammaSlider.setRange(int(0), int(100))
        self.gammaSaturationScale = 50
        self.gammaSlider.setValue(self.gammaSaturationScale)

        self.blurSlider.setRange(int(1), int(10))
        self.blurSaturationScale = 5
        self.blurSlider.setValue(self.blurSaturationScale)

        self.bilateralSlider_1.setRange(int(1), int(100))
        self.bilateralSlider_2.setRange(int(1), int(25))
        self.bilateralSaturationScale_1 = 1
        self.bilateralSaturationScale_2 = 1
        self.bilateralSlider_1.setValue(self.bilateralSaturationScale_1)
        self.bilateralSlider_2.setValue(self.bilateralSaturationScale_2)

        self.cartoonSlider.setRange(int(1), int(50))
        self.cartoonSaturationScale = 25
        self.cartoonSlider.setValue(self.cartoonSaturationScale)

        self.gaussianSlider.setRange(int(1), int(10))
        self.gaussianSaturationScale = 1
        self.gaussianSlider.setValue(self.gaussianSaturationScale)

        self.gammaSlider_2.setRange(int(0), int(100))
        self.gammaSlider_2.setValue(self.gammaSaturationScale)

        self.blurSlider_2.setRange(int(1), int(10))
        self.blurSlider_2.setValue(self.blurSaturationScale)

        self.cartoonSlider_2.setRange(int(1), int(50))
        self.cartoonSlider_2.setValue(self.cartoonSaturationScale)

        self.gaussianSlider_2.setRange(int(1), int(10))
        self.gaussianSlider_2.setValue(self.gaussianSaturationScale)

        self.label.setText("")

        self.optionStream.hide()
        self.optionImage.hide()
        self.optionVideo.show()

    def Blur_Filter(self):
        if self.rbStream.isChecked() or self.rbVideo.isChecked():
            self.blurSaturationScale = self.blurSlider.value()
        elif self.rbImage.isChecked() :
            self.blurSaturationScale = self.blurSlider_2.value()

        self.frame = cv2.blur(self.frame, (self.blurSaturationScale, self.blurSaturationScale))

    def Bilateral_Filter(self): # 애는 너무 느려서 이미지에만 쓴다
        self.bilateralSaturationScale_1 = self.bilateralSlider_1.value()
        self.bilateralSaturationScale_2 = self.bilateralSlider_2.value()
        self.frame = cv2.bilateralFilter(self.frame, -1, int(self.bilateralSaturationScale_1), int(self.bilateralSaturationScale_2))

    def Cartoon_Filter(self):
        img = self.frame
        h, w = img.shape[:2]
        img2 = cv2.resize(self.frame, (w//2, h//2))

        if self.rbStream.isChecked() or self.rbVideo.isChecked():
            sigma = self.cartoonSlider.value()
        elif self.rbImage.isChecked() :
            sigma = self.cartoonSlider_2.value()
        

        blr = cv2.bilateralFilter(img2, -1, sigma, 7)
        edge = 255 - cv2.Canny(img2, 80, 120)
        edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
        dst = cv2.bitwise_and(blr, edge)
        self.frame = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)

    def Gaussian_Filter(self):
        if self.rbStream.isChecked() or self.rbVideo.isChecked():
            sigma = self.gaussianSlider.value()
        elif self.rbImage.isChecked() :
            sigma = self.gaussianSlider_2.value()

        self.frame = cv2.GaussianBlur(self.frame, (0, 0), sigma)

    def HSV(self):
        if self.rbStream.isChecked() or self.rbVideo.isChecked():
            self.gammaSaturationScale = self.gammaSlider.value()
        elif self.rbImage.isChecked() :
            self.gammaSaturationScale = self.gammaSlider_2.value()

        hsvImage = cv2.cvtColor(self.frame, cv2.COLOR_RGB2HSV) 
        hsvImage = np.float32(hsvImage)
        H, S, V = cv2.split(hsvImage)
        S = np.clip( S * (self.gammaSaturationScale / 100) , 0,255 ) # 계산값, 최소값, 최대값
        hsvImage = cv2.merge( [ H,S,V ] )
        hsvImage = np.uint8(hsvImage)

        self.frame = cv2.cvtColor(hsvImage, cv2.COLOR_HSV2RGB)

    def Histogram_Filter(self):
        hsv = cv2.cvtColor(self.frame, cv2.COLOR_RGB2HSV)
        hsv[:,:,2] = cv2.equalizeHist(hsv[:,:,2])
        self.frame = cv2.cvtColor(hsv,cv2.COLOR_HSV2RGB)

    def Sketch_Filter(self):
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        blr = cv2.GaussianBlur(gray, (0, 0), 3)
        self.frame = cv2.divide(gray, blr, scale=255)

    def Stream_clicked(self):
        self.optionStream.setTitle("Streaming Option")
        self.optionStream.show()
        self.optionImage.hide()
        self.optionVideo.hide()

    def Video_clicked(self):
        self.optionStream.setTitle("Video Option")
        self.optionStream.show()
        self.optionImage.hide()
        self.optionVideo.hide()

    def Image_clicked(self):
        self.optionStream.hide()
        self.optionStream.hide()
        self.optionImage.show()
        self.optionVideo.hide()

    def updateMovie(self):
        retval, self.frame = self.cap.read()
        if retval:
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)  

            h, w, c, = self.frame.shape
            self.qimage = QImage(self.frame.data, w, h, w*c, QImage.Format_RGB888)

            self.pixmap = self.pixmap.fromImage(self.qimage)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

            self.label.setPixmap(self.pixmap)
            print(retval, self.frame)
        else :
            print("over")
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
        if (self.recCount > 14) and (self.record.running == True):
            self.recStat.hide()
            self.recCount = 0
        elif (self.recCount >= 7) and (self.record.running == True):
            self.recStat.show()
        elif (self.record.running == False):
            self.recStat.hide()
            self.recCount = 0

        self.recCount += 1
        self.writer.write(cv2.cvtColor(self.frame, cv2.COLOR_RGB2BGR))

    def recordingStart(self):
        self.record.running = True
        self.record.start()
        self.rbStream.setChecked(True)

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
            self.rbStream.setChecked(True)
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
        print(self.video)
        self.video.release()
        self.recStat.hide()
        if self.isRecStart == True:
            self.writer.release()

    def fileUpdating(self):
        if str(self.file[0]) != '':
            self.frame = cv2.imread(self.file[0])
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)

            if self.chBlur_2.isChecked():
                self.Blur_Filter()
            if self.chBilateral_2.isChecked():
                self.Bilateral_Filter()
            if self.chCartoon_2.isChecked():
                self.Cartoon_Filter()
            if self.chGaussian_2.isChecked():
                self.Gaussian_Filter()
            if self.chGamma_2.isChecked():
                self.HSV()
            if self.chHistogram_2.isChecked():
                self.Histogram_Filter()
            if self.chSketch_2.isChecked():
                self.Sketch_Filter()

            h, w, c = self.frame.shape
            qimage = QImage(self.frame.data, w, h, w*c, QImage.Format_RGB888)

            self.pixmap = self.pixmap.fromImage(qimage)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

            self.label.setPixmap(self.pixmap)
        else :
            pass

    def openFile(self):
        self.file = QFileDialog.getOpenFileName(self, '', '../data/', filter='Image (*.*)')

        self.record.stop()
        self.camera.stop()
        self.btnRecord.hide()
        self.btnCapture.show()

        self.cameraStart()
        if self.camera.running ==  True:
            self.cameraStop()
        else :
            pass
        
        print("21#!@#$!@$$#@", self.file[0], "@!#!@$#%#$")
        if self.file[0][-4:] == '.avi' or self.file[0][-4:] == '.mp4' or self.file[0][-4:] == '.mkv' or self.file[0][-4:] == '.mpg':
            self.movie.running = True
            self.movie.start()
            self.rbVideo.setChecked(True)
            play_url = self.file[0]
            self.cap = cv2.VideoCapture(play_url)
            pass
        elif str(self.file[0]) != '':
            self.rbImage.setChecked(True)
            self.frame = cv2.imread(self.file[0])
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)

            h, w, c = self.frame.shape
            qimage = QImage(self.frame.data, w, h, w*c, QImage.Format_RGB888)

            self.pixmap = self.pixmap.fromImage(qimage)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

            self.label.setPixmap(self.pixmap)

            self.fileUpdate.start()
        else :
            pass

    def updateCamera(self):
        retval, self.frame = self.video.read()

        if self.chBlur.isChecked():
            self.Blur_Filter()
        # if self.chBilateral.isChecked():
        #     self.Bilateral_Filter()
        if self.chCartoon.isChecked():
            self.Cartoon_Filter()
        if self.chGaussian.isChecked():
            self.Gaussian_Filter()
        if self.chGamma.isChecked():
            self.HSV()
        if self.chHistogram.isChecked():
            self.Histogram_Filter()
        if self.chSketch.isChecked():
            self.Sketch_Filter()

        if retval:
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)  

            h, w, c, = self.frame.shape
            self.qimage = QImage(self.frame.data, w, h, w*c, QImage.Format_RGB888)

            self.pixmap = self.pixmap.fromImage(self.qimage)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

            self.label.setPixmap(self.pixmap)

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