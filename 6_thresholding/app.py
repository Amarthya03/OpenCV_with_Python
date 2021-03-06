import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

greyscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(greyscaled, 12, 255, cv2.THRESH_BINARY)

gauss = cv2.adaptiveThreshold(greyscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('Original', img)
cv2.imshow('Threshold', threshold)
cv2.imshow('Greyscaled Threshold', threshold2)
cv2.imshow('Gauss', gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()