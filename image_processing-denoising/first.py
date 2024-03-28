import cv2 as cv

# ---------------------------------------------first--------------------------------------
# img1=cv.imread('a.tif')
# img2=cv.imread('b.tif')
# img1=cv.cvtColor(img1,cv.COLOR_RGB2GRAY)
# img2=cv.cvtColor(img2,cv.COLOR_RGB2GRAY)
# img1=-img1
# img2=-img2
# img1=img1-img2
# # x=cv.resize(x,(500,500))
# cv.imshow('result', img1)
# cv.waitKey()
# ---------------------------------------------two---------------------------------
import numpy as np

images = []
k = 0
for i in range(6):
    images.append(cv.imread('1/' + str(i + 1) + '.jpg'))
    images[i] = cv.cvtColor(images[i], cv.COLOR_RGB2GRAY)
    images[i] = images[i] // 5
    k += images[i]

pp = []
p2 = 0
for i in range(5):
    pp.append(cv.imread('2/' + str(i + 1) + '.jpg'))
    pp[i] = cv.cvtColor(pp[i], cv.COLOR_RGB2GRAY)
    pp[i] = pp[i] // 5
    p2 += pp[i]

pp = []
p3 = 0
for i in range(5):
    pp.append(cv.imread('3/' + str(i + 1) + '.jpg'))
    pp[i] = cv.cvtColor(pp[i], cv.COLOR_RGB2GRAY)
    pp[i] = pp[i] // 5
    p3 += pp[i]

pp = []
p4 = 0
for i in range(5):
    pp.append(cv.imread('4/' + str(i + 1) + '.jpg'))
    pp[i] = cv.cvtColor(pp[i], cv.COLOR_RGB2GRAY)
    pp[i] = pp[i] // 5
    p4 += pp[i]

a = cv.hconcat([k, p2])
b = cv.hconcat([p3, p4])
c = cv.vconcat([a, b])
c = cv.resize(c, (500, 500))

cv.imshow('Black hole', c)
cv.waitKey()