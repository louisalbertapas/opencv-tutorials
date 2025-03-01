import cv2
import numpy as np

img = cv2.imread('../chessboard.png')

cv2.imshow('image', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cornerHarris uses float32
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

dst = cv2.dilate(dst, None)

# mark the corners
img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow('dst', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
