import cv2 as cv
import numpy as np
img = cv.imread('chess pieces.jpg')
img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

m = []
count = 0
images = []
for column_num in range(img.shape[1]):
    column_data = []
    for i in range(img.shape[0]):
        if img[i, column_num] > 200:
            column_data.append(img[i, column_num])
    if len(column_data) == img.shape[0]:
        count += 1
    else:
        m.append(img[:, column_num])

    if count > 10 and len(m) > 10:
        images.append(m)


for i in range(len(images)):
    res = np.zeros([images[i][0].shape[0], len(images[i])], dtype=np.uint8)
    for j in range(len(images[i])):
        res[:j] = images[i][j]
    cv.imwrite(f'hw2/chess/chess{i}.jpg', res)