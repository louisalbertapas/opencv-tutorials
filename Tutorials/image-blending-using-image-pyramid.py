import cv2
import numpy as np

apple = cv2.imread('../apple.jpg')
orange = cv2.imread('../orange.jpg')

print(apple.shape)
print(orange.shape)

apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

# generate gaussian pyramid
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(5):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(5):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# generate laplacian pyramid
apple_copy = gp_apple[5]
lp_apple = [apple_copy]

for i in range(5, 0, -1):
    expanded = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i - 1], expanded)
    lp_apple.append(laplacian)

orange_copy = gp_orange[5]
lp_orange = [orange_copy]

for i in range(5, 0, -1):
    expanded = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i - 1], expanded)
    lp_orange.append(laplacian)

# join the half of these images
apple_orange_pyramid = []
n = 0

for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

# reconstruct the image
apple_orange_reconstructed = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstructed = cv2.pyrUp(apple_orange_reconstructed)
    apple_orange_reconstructed = cv2.add(apple_orange_pyramid[i], apple_orange_reconstructed)

cv2.imshow('apple', apple)
cv2.imshow('orange', orange)
cv2.imshow('apple_orange', apple_orange)
cv2.imshow('apple_orange_reconstructed', apple_orange_reconstructed)

cv2.waitKey(0)
cv2.destroyAllWindows()
