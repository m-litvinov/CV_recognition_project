import cv2 as cv
# import numpy as np

img = cv.imread("face.jpg", -1)

# Для детектирования лиц используем каскады Хаара
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(cascadePath)

# Для распознавания используем локальные бинарные шаблоны
recognizer = cv.createLBPHFaceRecognizer(1, 8, 8, 8, 123)

cv.namedWindow('face', cv.WINDOW_NORMAL)
cv.imshow('face', img)
k = 0
while (k != 27) & (k != ord('s')):
    k = cv.waitKey(0)  # записываем значение нажатой клавиши
    if k == 27:  # нажали ESC
        cv.destroyAllWindows()
        print('ESC pressed')
    elif k == ord("s"):  # нажали S для сохранения
        cv.imwrite("grey_face.png", img)
        cv.destroyAllWindows()
        print("'s' pressed")
    else:
        print("fail")
