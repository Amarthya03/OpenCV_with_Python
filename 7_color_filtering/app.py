import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# lower_red = np.array([0, 70, 50])
	# upper_red = np.array([10, 255, 255])

	# mask = cv2.inRange(hsv, lower_red, upper_red)
	# res = cv2.bitwise_and(frame, frame, mask=mask)

	# kernel = np.ones((15, 15), np.float32)/225
	# smoothed = cv2.filter2D(res, -1, kernel)
	# gauss = cv2.GaussianBlur(res, (15, 15), 0)
	# median = cv2.medianBlur(res, 15)
	# bliateral = cv2.bilateralFilter(res, 15, 75, 75)
	# kernel = np.ones((5, 5), np.uint8)
	# erosion = cv2.dilate(mask, kernel, iterations=1)
	# dilation = cv2.dilate(mask, kernel, iterations=1)

	# opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	# closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)



	# cv2.imshow('Output', frame)
	# cv2.imshow('Mask', mask)
	# cv2.imshow('Res', res)
	# cv2.imshow('Smoothed', smoothed)
	# cv2.imshow('Gaussian Blur', gauss)
	# cv2.imshow('Median Blur', median)
	# cv2.imshow('bilateral', bliateral)
	# cv2.imshow('Erosion', erosion)
	# cv2.imshow('Dilation', dilation)
	# cv2.imshow('Opening', opening)
	# cv2.imshow('Closing', closing)

	laplacian = cv2.Laplacian(frame, cv2.CV_64F)
	sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
	sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
	edges = cv2.Canny(frame, 100, 200)

	cv2.imshow('original', frame)
	cv2.imshow('laplacian', laplacian)
	cv2.imshow('Sobel X', sobelx)
	cv2.imshow('Sobel Y', sobely)
	cv2.imshow('Edges', edges)


	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()