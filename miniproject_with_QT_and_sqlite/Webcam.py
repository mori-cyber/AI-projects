import cv2
from Filtering import Filter
# from main import AddUser
from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QSize
from PySide6 import QtGui
from functools import partial


class Camera(QWidget):
    def __init__(self, num, lbl_photo):
        super(Camera, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('Filter_Pic.ui')
        self.ui.show()
        self.ui.Q1_1.clicked.connect(partial(self.savePhoto, 1))
        self.ui.Q1_2.clicked.connect(partial(self.savePhoto, 2))
        self.ui.Q1_3.clicked.connect(partial(self.savePhoto, 3))
        self.ui.Q1_4.clicked.connect(partial(self.savePhoto, 4))
        self.ui.Q1_5.clicked.connect(partial(self.savePhoto, 5))
        self.ui.Q1_6.clicked.connect(partial(self.savePhoto, 6))
        self.ui.Q1_7.clicked.connect(partial(self.savePhoto, 6))
        self.ui.Q1_8.clicked.connect(partial(self.savePhoto, 7))
        self.ui.Q1_9.clicked.connect(partial(self.savePhoto, 8))
        self.num = num
        self.lbl_photo = lbl_photo

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        video = cv2.VideoCapture(0)

        while True:
            validation, frame = video.read()

            if validation is not True:
                break

            faces = face_cascade.detectMultiScale(frame, 1.3, 4)
            for (x, y, w, h) in faces:
                img = frame[y:y + h, x:x + w]
                self.width = w
                self.height = h
                self.x = x
                self.y = y

            self.frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            self.blured_photo = Filter(self.frame).blur()
            self.img1 = QtGui.QImage(self.blured_photo, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            self.pix1 = QtGui.QPixmap.fromImage(self.img1)
            self.ui.Q1_1.setIcon(QtGui.QIcon(self.pix1))
            self.ui.Q1_1.setIconSize(QSize(200, 200))

            self.light_photo = Filter(self.frame).moreLigth()
            self.img2 = QtGui.QImage(self.light_photo, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            self.pix2 = QtGui.QPixmap.fromImage(self.img2)
            self.ui.Q1_2.setIcon(QtGui.QIcon(self.pix2))
            self.ui.Q1_2.setIconSize(QSize(200, 200))

            self.sketch_photo = Filter(self.frame).flip()
            self.img3 = QtGui.QImage(self.sketch_photo, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            self.pix3 = QtGui.QPixmap.fromImage(self.img3)
            self.ui.Q1_3.setIcon(QtGui.QIcon(self.pix3))
            self.ui.Q1_3.setIconSize(QSize(200, 200))

            self.bw_photo = Filter(self.frame).blackAndWithe()
            self.img4 = QtGui.QImage(self.bw_photo, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            self.pix4 = QtGui.QPixmap.fromImage(self.img4)
            self.ui.Q1_4.setIcon(QtGui.QIcon(self.pix4))
            self.ui.Q1_4.setIconSize(QSize(200, 200))

            self.nored_photo = Filter(self.frame).noRed()
            self.img5 = QtGui.QImage(self.nored_photo, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            self.pix5 = QtGui.QPixmap.fromImage(self.img5)
            self.ui.Q1_5.setIcon(QtGui.QIcon(self.pix5))
            self.ui.Q1_5.setIconSize(QSize(200, 200))

            self.noblue_photo = Filter(self.frame).noBlue()
            self.img6 = QtGui.QImage(self.noblue_photo, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            self.pix6 = QtGui.QPixmap.fromImage(self.img6)
            self.ui.Q1_6.setIcon(QtGui.QIcon(self.pix6))
            self.ui.Q1_6.setIconSize(QSize(200, 200))

            self.nogreen_photo = Filter(self.frame).noGreen()
            self.img7 = QtGui.QImage(self.nogreen_photo, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            self.pix7 = QtGui.QPixmap.fromImage(self.img7)
            self.ui.Q1_7.setIcon(QtGui.QIcon(self.pix7))
            self.ui.Q1_7.setIconSize(QSize(200, 200))

            self.inv_photo = Filter(self.frame).inverte()
            self.img8 = QtGui.QImage(self.inv_photo, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            self.pix8 = QtGui.QPixmap.fromImage(self.img8)
            self.ui.Q1_8.setIcon(QtGui.QIcon(self.pix8))
            self.ui.Q1_8.setIconSize(QSize(200, 200))

            self.filtered_photo = Filter(self.frame).threeColor()
            self.img9 = QtGui.QImage(self.filtered_photo, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            self.pix9 = QtGui.QPixmap.fromImage(self.img9)
            self.ui.Q1_9.setIcon(QtGui.QIcon(self.pix9))
            self.ui.Q1_9.setIconSize(QSize(200, 200))

            cv2.imshow('output', img)
            cv2.waitKey(1)

    def savePhoto(self, n):
        if n == 1:
            photo = self.blured_photo
        elif n == 2:
            photo = self.light_photo
        elif n == 3:
            photo = self.sketch_photo
        elif n == 4:
            photo = self.bw_photo
        elif n == 5:
            photo = self.noblue_photo
        elif n == 6:
            photo = self.nored_photo
        elif n == 7:
            photo = self.nogreen_photo
        elif n == 8:
            photo = self.inv_photo
        else:
            photo = self.filtered_photo

        cv2.imwrite(f"assets/img/users/{self.num}.jpg", photo[self.y:self.y + self.height, self.x:self.x + self.width])
        self.lbl_photo.setPixmap(f"assets/img/users/{self.num}.jpg")