import cv2
import numpy as np




image  = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)

image = cv2.resize(image,(500,500))

mask = np.ones((7,7), dtype=float) / 49
print(mask)

result = np.zeros(image.shape,dtype='uint8')

for i in range(3,image.shape[0]-3):
    for j in range(3,image.shape[1]-3):
        image_box = image[i-3:i+4,j-3:j+4]
        result[i,j] = np.sum(np.multiply(image_box,mask))


cv2.imshow('out_put',result)
cv2.waitKey()