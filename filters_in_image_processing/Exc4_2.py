import cv2
import numpy as np




image  = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)

image = cv2.resize(image,(500,500))

mask = np.ones((5,5), dtype=float) / 25
print(mask)
# image = cv2.resize(image,(256,256))
result = np.zeros(image.shape,dtype='uint8')

for i in range(2,image.shape[0]-2):
    for j in range(2,image.shape[1]-2):
        image_box = image[i-2:i+3,j-2:j+3]
        result[i,j] = np.sum(np.multiply(image_box,mask))


cv2.imshow('out_put',result)
cv2.waitKey()