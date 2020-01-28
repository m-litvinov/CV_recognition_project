import cv2 as cv
import numpy as np
import os
from PIL import Image


def get_images(path):
    image_paths = [
        os.path.join(path, f) for f in os.listdir(path)
        if not f.endswith('.happy')]

    images = []
    labels = []

    for image_path in image_paths:
        gray = Image.open(image_path).convert('L')
        img = np.array(gray, 'uint8')
        # img = cv.imread(image_path, 0)

        subject_number = int(
            os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
        faces = faceCascade.detectMultiScale(
            img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            images.append(img[y: y + h, x: x + w])
            labels.append(subject_number)

            # cv.imshow("face", img[y: y + h, x: x + w])
            # cv.waitKey(50)
    return images, labels


cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(cascadePath)

recognizer = cv.face.LBPHFaceRecognizer_create(1, 8, 8, 8, 123)

path = './yalefaces'
images, labels = get_images(path)
cv.destroyAllWindows()

print("Training model")
recognizer.update(images, np.array(labels))

subject_name = ""

print("Let see you now")
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # set frame size
    ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT, 320)
    ret = cap.set(cv.CAP_PROP_FRAME_WIDTH, 240)

    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # trying detect faces on frame
    faces = faceCascade.detectMultiScale(
        frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        subject_predicted, conf = recognizer.predict(frame[y: y + h, x: x + w])
        # dividing known and unknown faces
        subject_actual = 16
        if subject_predicted == 16:
            subject_name = "Mike"
        else:
            subject_name = "Unknown"

        img_font = cv.FONT_HERSHEY_SIMPLEX
        if subject_actual == subject_predicted:
            print(f"{subject_name} is correctly recognized \
with confidence {conf}")

            frame = cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv.putText(
                frame, subject_name, (x, y-10),
                img_font, 2, (255, 0, 0), 2, cv.LINE_AA)

        else:
            print(f"{subject_actual} is incorrect recognized \
as {subject_predicted}")
            frame = cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv.putText(
                frame, subject_name, (x, y-20),
                img_font, 2, (255, 0, 0), 2, cv.LINE_AA)

    cv.imshow("face", frame)
    # wait for ESC
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv.destroyAllWindows
