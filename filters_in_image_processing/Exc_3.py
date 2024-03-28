import cv2
import numpy as np




image  = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)



mask = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
print(mask)

image = cv2.resize(image,(256,256))

print(image.shape)

result = np.zeros((256,256),dtype='uint8')
rows,cols = image.shape
for i in range(1,rows-1):
    for j in range(1, cols-1):
        image_box = image[i-1:i+2,j-1:j+2]
        mul_result = np.multiply(image_box,mask)
        out = np.sum(mul_result)
        result[i, j] = out
cv2.imshow('out_put',result)
cv2.waitKey()