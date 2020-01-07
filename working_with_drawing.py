import numpy as np
import cv2 as cv

img = cv.imread("photo.jpg", -1)

# Draw the blue line
# Line
cv.line(img, (0,0), (img.shape[1], img.shape[0]), (255,0,0),5)
# Rectangle
cv.rectangle(img,(768, 0), (1024, 315),(0,255,0), 3)
# Circle
cv.circle(img, (896, 157), 100, (0,0,255), -1)
# Text
img_font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "Root", (0, 512), img_font, 4, (255,255,0), 4, cv.LINE_AA)

cv.imshow("image", img)

cv.waitKey(0)
cv.destroyAllWindows