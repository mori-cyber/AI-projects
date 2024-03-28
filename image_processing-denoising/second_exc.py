import cv2 as cv
# import numpy as np
#
# images = [[0 for i in range(5)] for j in range(4)]
#
# for i in range(4):
#     for j in range(5):
#         images[i][j] = cv.imread(str(i + 1) + '/' + str(j + 1) + '.jpg')
#         images[i][j] = cv.cvtColor(images[i][j], cv.COLOR_BGR2GRAY)
#
# image_without_noise = [0 for i in range(4)]
#
# for i in range(4):
#     for j in range(5):
#         image_without_noise[i] = image_without_noise[i] + (images[i][j] / 5)
#
# final_image = np.zeros((2000, 2000), dtype=np.uint8)
#
# final_image[0:1000, 0:1000] = image_without_noise[0]
# final_image[0:1000, 1000:2000] = image_without_noise[1]
# final_image[1000:2000, 0:1000] = image_without_noise[2]
# final_image[1000:2000, 1000:2000] = image_without_noise[3]
#
# cv.imshow('Final Image', final_image)
#
# cv.imwrite('final_image.jpg', final_image)
#
# cv.waitKey()

images1 = []
k1 = 0
for i in range(5):
    images1.append(cv.imread('1/' + str(i + 1) + '.jpg'))
    images1[i] = cv.cvtColor(images1[i], cv.COLOR_RGB2GRAY)
    images1[i] = images1[i] // 5
    k1 += images1[i]

images2 = []
k2 = 0
for i in range(5):
    images2.append(cv.imread('2/' + str(i + 1) + '.jpg'))
    images2[i] = cv.cvtColor(images2[i], cv.COLOR_RGB2GRAY)
    images2[i] = images2[i] // 5
    k2 += images2[i]

images3 = []
k3 = 0
for i in range(5):
    images3.append(cv.imread('3/' + str(i + 1) + '.jpg'))
    images3[i] = cv.cvtColor(images3[i], cv.COLOR_RGB2GRAY)
    images3[i] = images3[i] // 5
    k3 += images3[i]

images4 = []
k4 = 0
for i in range(5):
    images4.append(cv.imread('4/' + str(i + 1) + '.jpg'))
    images4[i] = cv.cvtColor(images4[i], cv.COLOR_RGB2GRAY)
    images4[i] = images4[i] // 5
    k4 += images4[i]

x = cv.hconcat([k1, k2])
y = cv.hconcat([k3, k4])
m = cv.vconcat([x, y])
m = cv.resize(m, (700, 700))

cv.imshow('the result', m)
cv.waitKey()