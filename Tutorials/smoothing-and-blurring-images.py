import cv2
import numpy as np
from matplotlib import pyplot as plt

# smoothing removes noise
# use linear filters

img = cv2.imread('../lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# homogeneuos filter
# output pixel = mean of its kernel neighbors
# it has equal weight
# knl = 1 / (kmatrix.width * kmatrix.height)
knl = np.ones((5, 5), np.float32) / 25
hf = cv2.filter2D(img, -1, knl)

# blur method / averaging
# (5, 5) kernel
blur = cv2.blur(img, (5, 5))

# gaussian filter
# different weight in x and y dimension
# designed to clean high frequency noise
gblur = cv2.GaussianBlur(img, (5, 5), 0)


# median filter
# replaces pixels value with the median of its neighboring pixel
# great when dealing "salt and pepper" noise
median = cv2.medianBlur(img, 5)

# bilateral filter
# noise removal while keeping the edge sharp
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image', '2D convolution', 'Blur', 'Gaussian Blur', 'Median Filter', 'Bilateral Filter']
images = [img, hf, blur, gblur, median, bilateralFilter]


for i in range(len(titles)):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
