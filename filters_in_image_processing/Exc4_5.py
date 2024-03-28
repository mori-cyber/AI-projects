import cv2
import numpy as np

image  = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)
# image  = cv2.imread('1.jpg')
# image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image = cv2.resize(image,(500,500))

# mask = np.ones((7,7), dtype=float) / 49
# print(mask)


def kernel(x,y,num):
    result = np.zeros(image.shape, dtype='uint8')
    mask = np.ones((x, y), dtype=float) / num
    if x==3 and num ==9:
        m=1
        n=2
    elif x==5 and num==25:
        m=2
        n=3
    elif x==7 and num == 49:
        m=3
        n=4
    elif x==15 and num == 225:
        m=7
        n=8
    else:
        print('no match number')
    for i in range(m, image.shape[0] - m):
        for j in range(m, image.shape[1] - m):
            image_box = image[i - m:i + n, j - m:j + n]
            result[i, j] = np.sum(np.multiply(image_box, mask))
    return  result

x =int(input('enter x mask:'))
y =int(input('enter y mask:'))
number =int(input('enter num div:'))
out_put = kernel(x,y,number)
cv2.imshow('out_put',out_put)
cv2.waitKey()