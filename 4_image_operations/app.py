import numpy as np
import cv2

img = cv2.imread('cole.jpg', cv2.IMREAD_COLOR)

px = img[55, 55]
print(px)

img[55, 55] = [255, 255, 255]
px = img[55, 55]
print(px)

# img[100:350, 200:350] = [255, 255, 255]

crop = img[100:350, 200:350]
img[200:450, 300:450] = crop

cv2.imshow('Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()