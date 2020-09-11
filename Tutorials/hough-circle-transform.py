import cv2
import numpy as np

img = cv2.imread('../smarties.png')
output = img.copy()
gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)

# hough circle works well in blurred images
# gray = cv2.GaussianBlur(gray, (5, 5), 1)
gray = cv2.medianBlur(gray, 5)

# hough circle method
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,
                           dp=1,
                           minDist=20,
                           param1=50,
                           param2=30,
                           minRadius=0,
                           maxRadius=0)

# convert the circles into x, y coords and r
detected_circles = np.uint16(np.around(circles))

for x, y, r in detected_circles[0, :]:
    cv2.circle(output, (x, y), r, (0, 255, 0), thickness=2)
    cv2.circle(output, (x, y), 2, (0, 255, 255), thickness=2)

cv2.imshow('image', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
