import cv2
import numpy as np
from matplotlib import pyplot as plt

# an image gradient is a directional change in the
# intensity or color in an image

img = cv2.imread('../sudoku.png', cv2.IMREAD_GRAYSCALE)

# laplace gradient
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))  # make it absolute

# sobelX
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))

# sobelY
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))

# combine sobel X and sobel Y
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['image', 'Laplacian', 'SobelX', 'SobelY', 'SobelCombined']
images = [img, lap, sobelX, sobelY, sobelCombined]

for i in range(len(titles)):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
