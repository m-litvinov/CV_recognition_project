import cv2 as cv
import numpy as np

img = cv.imread("photo.jpg", 0)

cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', img)
k = 0
while (k != 27) & (k != ord('s')):
    k = cv.waitKey(0) # записываем значение нажатой клавиши
    if k == 27: # нажали ESC
        cv.destroyAllWindows()
        print('ESC pressed')
    elif k == ord("s"): # нажали S для сохранения
        cv.imwrite("grey_photo.png", img)
        cv.destroyAllWindows()
        print("'s' pressed")
    else:
        print("fail")
