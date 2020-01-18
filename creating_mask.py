import numpy as np
import cv2 as cv


def nothing(*args):
    pass


cap = cv.VideoCapture(0)

cv.namedWindow("settings")

cv.createTrackbar("h1", "settings", 0, 255, nothing)
cv.createTrackbar("s1", "settings", 0, 255, nothing)
cv.createTrackbar("v1", "settings", 0, 255, nothing)
cv.createTrackbar("h2", "settings", 255, 255, nothing)
cv.createTrackbar("s2", "settings", 255, 255, nothing)
cv.createTrackbar("v2", "settings", 255, 255, nothing)

while True:
    ret, frame = cap.read()
    # set frame size
    ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT, 320)
    ret = cap.set(cv.CAP_PROP_FRAME_WIDTH, 240)

    # add parameter control
    h1 = cv.getTrackbarPos("h1", "settings")
    s1 = cv.getTrackbarPos("s1", "settings")
    v1 = cv.getTrackbarPos("v1", "settings")
    h2 = cv.getTrackbarPos("h2", "settings")
    s2 = cv.getTrackbarPos("s2", "settings")
    v2 = cv.getTrackbarPos("v2", "settings")

    # convert image color-space to HSV, else - BGR
    # hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # set color range for mask
    lower_color = np.array([h1, s1, v1])
    upper_color = np.array([h2, s2, v2])

    # create mask from this range
    mask = cv.inRange(frame, lower_color, upper_color)

    # use bitwise AND for adding regular image with mask
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)
    # wait for ESC
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv.destroyAllWindows
