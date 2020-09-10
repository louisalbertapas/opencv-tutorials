import cv2
import numpy as np

img = cv2.imread('../messi5.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('../messi5-face.jpg', cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]  # gets the column and rows

res = cv2.matchTemplate(gray, template, cv2.TM_CCORR_NORMED)
print(res)
threshold = 0.99
loc = np.where(res >= threshold)  # return res that are greater than threshold
print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
