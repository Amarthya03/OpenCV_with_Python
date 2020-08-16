import cv2
import numpy as np

img_bgr = cv2.imread('fcb.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread('logo.jpg', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.6
loc = np.where(res>=threshold)
count = 0

for pt in zip(*loc[::-1]):
	count = count + 1
	cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 2)

print(count)
imS = cv2.resize(img_bgr, ((1440//2), 450))
cv2.imshow('Output', imS)
cv2.waitKey(0)
cv2.destroyAllWindows()
