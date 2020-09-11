import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# take first frame
ret, frame = cap.read()

# find the initial location to track
x, y, w, h = 300, 200, 100, 50
track = (x, y, w, h)

# histogram back projected
# setup ROI for tracking
roi = frame[y: y + h, x: x + w]

# hsv color space
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# mask
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255)))

# calculate histogram
roi_hist = cv2.calcHist([hsv_roi], [0], mask, histSize=[180], ranges=[0, 180])

# normalize between 0 to 255
cv2.normalize(roi_hist, roi_hist, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# criteria
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # back projected image
        dst = cv2.calcBackProject([hsv], channels=[0], hist=roi_hist, ranges=[0, 180], scale=1)

        # mean shift
        # ret, track = cv2.meanShift(dst, window=track, criteria=term_criteria)

        # camshift
        ret, track = cv2.CamShift(dst, window=track, criteria=term_criteria)

        # draw it on image
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)  # convert to integer
        frame = cv2.polylines(frame, [pts], isClosed=True, color=(0, 255, 0), thickness=3)
        # x, y, w, h = track
        # frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
        cv2.imshow('dst', dst)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()