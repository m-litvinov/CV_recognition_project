import numpy
import cv2 as cv

img = cv.imread("photo.jpg", -1)

low_blue = numpy.array((90,20,20), numpy.uint8)
high_blue = numpy.array((150,255,255), numpy.uint8)

img_hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)

cv.imshow("Image", img_hsv)

cv.waitKey(0)
cv.destroyAllWindows()