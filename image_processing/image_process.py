import sys
import os
import numpy as np
from scipy.ndimage import morphology
import matplotlib.pyplot as plt

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

import cv2 as cv

class Image_process(QWidget):
    def __init__(self):
        super(Image_process, self).__init__()

        loader = QUiLoader()
        self.ui = loader.load("form.ui")

        self.ui.pb_1.clicked.connect(self.chees)
        self.ui.pb_2.clicked.connect(self.image1)
        self.ui.pb_3.clicked.connect(self.image2)
        self.ui.pb_4.clicked.connect(self.rotate_im)
        # self.ui.pb_3.clicked.connect(self.algorithm)
        self.ui.show()
    def algorithm(self):
        img = cv.imread('4.png')
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        gray_r = img.reshape(img.shape[0] * img.shape[1])
        for i in range(gray_r.shape[0]):
            if gray_r[i] > gray_r.mean():
                gray_r[i] = 1
            else:
                gray_r[i] = 0
        gray = gray_r.reshape(img.shape[0], img.shape[1])
        plt.imshow(img, cmap='gray')
    def rotate_im(self):
        self.img = cv.imread('3.jpg')
        img = cv.resize(self.img, (500, 500))
        window_name = 'Image'

        image = cv.rotate(img, cv.ROTATE_180)

        cv.imshow(window_name, image)
        cv.waitKey(0)

    def image2(self):

        img = cv.imread('2.jpg')
        img = cv.resize(img, (500, 500))
        rows = img.shape[0]
        cols = img.shape[1]

        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        for i in range(rows):
            for j in range(cols):
                img[i, j] = 255 - img[i, j]

        cv.imshow('chess', img)
        cv.waitKey()
    def image1(self):
        img = cv.imread('1.jpg')
        rows = img.shape[0]
        cols = img.shape[1]

        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        for i in range(rows):
            for j in range(cols):
                img[i, j] = 255 - img[i, j]

        cv.imshow('chess', img)
        cv.waitKey()
    def chees(self):
        img = cv.imread('original_result.png')
        rows = img.shape[0]
        cols = img.shape[1]

        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        for i in range(rows):
            for j in range(cols):
                img[i, j] = 255 - img[i, j]

        cv.imshow('chess', img)
        cv.waitKey()
if __name__ == "__main__":
    app = QApplication([])
    widget = Image_process()
    sys.exit(app.exec_())