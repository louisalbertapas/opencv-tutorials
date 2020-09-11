import cv2
import numpy as np

cap = cv2.VideoCapture('../vtest.avi')

# fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
fgbg = cv2.createBackgroundSubtractorKNN()

while cap.isOpened():
    _, frame = cap.read()
    if frame is None:
        break

    # get foreground mask
    fgmask = fgbg.apply(frame)

    cv2.imshow('frame', frame)
    cv2.imshow('fg frame', fgmask)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
