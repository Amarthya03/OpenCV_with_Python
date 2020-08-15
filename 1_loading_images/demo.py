import cv2
import numpy as numpy
import matplotlib.pyplot as plt

img = cv2.imread('elle.jpg', cv2.IMREAD_GRAYSCALE)
# * IMREAD_COLOR = 1
# * IMREAD_UNCHANGED = -1

# ? Image rendering using OpenCV
cv2.imshow('image', img) # ? Title of image
cv2.waitKey(0) # ? Waits for any key to be pressed
cv2.destroyAllWindows()

# ? Image rendering using Matplotlib
# plt.imshow(img, cmap='gray')
# plt.plot([50, 100], [80, 100], 'y', linewidth=6)
# plt.show()

# ? To save image in the directory
cv2.imwrite('elle2.png', img)