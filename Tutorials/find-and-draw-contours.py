import cv2
import numpy as np

img = cv2.imread('../smarties.png')
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply threshold
ret, thresh = cv2.threshold(imggray, 127, 255, 0)

# find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# contours is a python list of all the contours found

print(str(len(contours)))

# -1 to draw all contours
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow('image', img)
cv2.imshow('image gray', imggray)

cv2.waitKey(0)
cv2.destroyAllWindows()
