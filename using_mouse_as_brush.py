import numpy as np
import cv2 as cv

img = cv.imread("photo.jpg", -1)

events = [i for i in dir(cv) if "EVENT" in i]
# print(events)

# set mouse callback
def circle_draw(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x,y), 100, (255,0,0),-1)

cv.namedWindow("image")
cv.setMouseCallback("image", circle_draw)

while True:
    cv.imshow("image", img)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows