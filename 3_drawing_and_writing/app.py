import numpy as np
import cv2

img = cv2.imread('greta.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0, 0), (150, 150), (120, 120, 0), 15)
cv2.rectangle(img, (15, 25), (300, 250), (0, 120, 120), 25)
cv2.circle(img, (25, 65), 120, (60, 60, 60), 30)

# pts = np.array([[300, 150], [600, 900], [1400, 600], [1000, 800]], np.int32)
# # pts = pts.reshape((-1, 1, 2))
# cv2.polylines(img, [pts], True, (0, 255, 120), 30)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Greta Gerwig', (00, 1200), font, 5, (0, 120, 120), 10, cv2.LINE_AA)

imS = cv2.resize(img, (300, 450))
cv2.imshow('Output', imS)
cv2.waitKey(0)
cv2.destroyAllWindows()