import cv2
import numpy as np




image  = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)

image = cv2.resize(image,(500,500))

mask = np.ones((3,3), dtype=float) / 9
print(mask)
# image = cv2.resize(image,(256,256))
result = np.zeros(image.shape,dtype='uint8')

for i in range(1,image.shape[0]-1):
    for j in range(1,image.shape[1]-1):
        image_box = image[i-1:i+2,j-1:j+2]
        result[i,j] = np.sum(np.multiply(image_box,mask))


cv2.imshow('out_put',result)
cv2.waitKey()