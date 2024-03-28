import cv2
import numpy as np




image  = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)

image = cv2.resize(image,(500,500))

mask = np.ones((15,15), dtype=float) / 225
print(mask)

result = np.zeros(image.shape,dtype='uint8')

for i in range(7,image.shape[0]-7):
    for j in range(7,image.shape[1]-7):
        image_box = image[i-7:i+8,j-7:j+8]
        result[i,j] = np.sum(np.multiply(image_box,mask))


cv2.imshow('out_put',result)
cv2.waitKey()