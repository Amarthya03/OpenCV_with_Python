import numpy as np
import cv2 as cv

img = cv.imread('marlon.jpg', 0)

# * CLAHE (Contrast Limited Adaptive Histogram Equalization)
# ? adaptive histogram equalization is used

clahe = cv.createCLAHE(clipLimit = 2.0, tileGridSize = (8, 8)) # ? image is divided into small blocks called "tiles" (tileSize is 8x8 by default in OpenCV)
cl1 = clahe.apply(img)

cv.imwrite('clahe_2.jpg', cl1)