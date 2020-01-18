import cv2 as cv

cap = cv.VideoCapture(0)

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(cascadePath)

faces = []

while True:
    ret, frame = cap.read()
    # set frame size
    ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT, 320)
    ret = cap.set(cv.CAP_PROP_FRAME_WIDTH, 240)

    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        frame = cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv.imshow("face", frame)
    # wait for ESC
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv.destroyAllWindows
