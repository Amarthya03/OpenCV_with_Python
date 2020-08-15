import cv2
import numpy as np 

# ? Reading a web-cam
# * Videos can be treated as a collection of frames

# ? Connecting to first camera
cap = cv2.VideoCapture(0)
src = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', src, 20.0, (640,480))

while(True):
	# ? Returning a collection of frames
	ret, frame = cap.read()

	# ? Converting frames to grayscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow('Frame', frame)
	# ? Rendering gray images
	cv2.imshow('Grayscale', gray)
	# ? Quit rendering images when 'Q' is pressed
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
out.release()
cv2.destroyAllWindows()
