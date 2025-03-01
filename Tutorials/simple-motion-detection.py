import cv2
import numpy as np

cap = cv2.VideoCapture('../vtest.avi')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)  # find the difference between frame1 and frame2

    # convert the diff to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # blur the grayscaled image
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # threshold
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # dilate the threshold image to fill the holes
    dilated = cv2.dilate(thresh, None, iterations=3)

    # find the contours
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # save the coordinate of each contour
        (x, y, w, h) = cv2.boundingRect(contour)

        # check the area of the contour
        if cv2.contourArea(contour) < 900:
            continue

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, 'Status: {}'.format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    cv2.imshow('video feed', frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()