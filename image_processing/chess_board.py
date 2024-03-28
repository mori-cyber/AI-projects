import cv
import cv2

import numpy as np
from scipy.ndimage import morphology

img = cv2.imread('4.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


close = 255 - cv2.morphologyEx(img, cv2.MORPH_CLOSE, img, iterations=2)
cv2.imshow("cleaned", close)
cv2.waitKey(0)
