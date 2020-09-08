import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../smarties.png', cv2.IMREAD_GRAYSCALE)

# mask since morphological needs to operate in binary
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# dilation increases the area
# kernel is a shape we want to apply in the image
knl = np.ones((5, 5), np.uint8)  # a 2x2 square

# iterations = number of times to perform dilation
dilation = cv2.dilate(mask, knl, iterations=2)

# erosion
# decreases the area based on the kernel
erosion = cv2.erode(mask, knl, iterations=1)

# opening
# erosion followed by dilation
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, knl)

# closing
# dilation followed by erosion
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, knl)

# gradient
# difference between dilation and erosion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, knl)

# top hat
# difference between image and opening
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, knl)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'gradient', 'tophat']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(len(titles)):
    plt.subplot(2, 4, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()