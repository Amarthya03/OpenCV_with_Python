import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')
img3 = cv2.imread('mainlogo.png')

rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]

img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img3gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img3_fg = cv2.bitwise_and(img3, img3, mask=mask)

dst = cv2.add(img1_bg, img3_fg)
img1[0:rows, 0:cols] = dst


cv2.imshow('Output', img1)
# ? Superimposing two images
# add = img1 + img2

# ? Using built-in OpenCV methods to add two images, the pixels
# get added to produce a much brighter image
# add = cv2.add(img1, img2)

# ? Adding images based off weights
# weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

# cv2.imshow('Output', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()