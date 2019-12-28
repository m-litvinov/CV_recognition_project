import cv2 as cv
import numpy

cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter("output.avi", fourcc, 20.0, (320, 240))

if not cap.isOpened():
    print("Cannot open the camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error recieve frame")
        break

    ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT, 320)
    ret = cap.set(cv.CAP_PROP_FRAME_WIDTH, 240)

    grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    out.write(grey) # Not working

    cv.imshow("webcam", grey)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()