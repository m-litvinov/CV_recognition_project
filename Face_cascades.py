import cv2 as cv
# import numpy as np

img = cv.imread("face.jpg", 0)

# Для детектирования лиц используем каскады Хаара
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(cascadePath)

images = []

faces = faceCascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# for (x, y, w, h) in faces:
#     images.append(img[y: y + h, x: x + w])

for (x, y, w, h) in faces:
    img = cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# В окне показываем изображение
cv.namedWindow('face', cv.WINDOW_NORMAL)
# cv.imshow("face", img[y: y + h, x: x + w])
cv.imshow("face", img)

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
