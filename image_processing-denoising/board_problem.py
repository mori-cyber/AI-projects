import cv2 as cv
O_img=cv.imread('board - origin.bmp')
T_img=cv.flip(cv.imread('board - test.bmp'),1)
O_img=cv.cvtColor(O_img,cv.COLOR_RGB2GRAY)
T_img=cv.cvtColor(T_img,cv.COLOR_RGB2GRAY)
result = cv.subtract(T_img, O_img)*5
resule=cv.resize(result,(300,300))
cv.imshow('resule_board',result)
cv.waitKey()
