import cv2
import numpy as np

# use image pyramids to handle images with different resolution

img = cv2.imread('../lena.jpg')

# gaussian pyramid
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i), layer)

# laplacian pyramid
layer = gp[5]
cv2.imshow('upper level Gaussian Pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_expanded = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_expanded)
    cv2.imshow(str(i), laplacian)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
