import cv2 as cv
img=[]
k=0
for i in range(15):
    img.append(cv.imread('h'+str(i)+'.jpg'))
    img[i]=cv.cvtColor(img[i],cv.COLOR_RGB2GRAY)
    img[i]=img[i]//15
    k+=img[i]

cv.imshow('result',k)
cv.waitKey()