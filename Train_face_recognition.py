import cv2 as cv
import numpy as np
import os


def get_images(path):
    image_paths = [
        os.path.join(path, f) for f in os.listdir(path)
        if not f.endswith('_happy')]

    images = []
    labels = []

    for image_path in image_paths:
        img = cv.imread(image_path, 0)
        # subject = image_path.split("_")[0]
        subject_number = 0

        faces = faceCascade.detectMultiScale(
            img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            images.append(img[y: y + h, x: x + w])
            # labels.append(subject)
            labels.append(subject_number)

            # cv.imshow("face", img[y: y + h, x: x + w])
            # cv.waitKey(50)
    return images, labels


cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(cascadePath)

recognizer = cv.face.LBPHFaceRecognizer_create()

path = './face'
images, labels = get_images(path)
cv.destroyAllWindows()
# TODO: Train model on larger dataset
print("Training model")
recognizer.train(images, np.array(labels))

cap = cv.VideoCapture(0)
subject_list = ['mike']

while True:
    ret, frame = cap.read()
    # set frame size
    ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT, 320)
    ret = cap.set(cv.CAP_PROP_FRAME_WIDTH, 240)

    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        subject_predicted, conf = recognizer.predict(frame[y: y + h, x: x + w])

        subject_actual = 0

        img_font = cv.FONT_HERSHEY_SIMPLEX
        if subject_actual == subject_predicted:
            print(f"{subject_list[subject_actual]} is correctly recognized \
with confidence {conf}")

            frame = cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv.putText(
                frame, subject_list[subject_predicted], (x, y-10),
                img_font, 2, (255, 0, 0), 2, cv.LINE_AA)

        else:
            print(f"{subject_actual} is incorrect recognized \
as {subject_predicted}")
            frame = cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv.putText(
                frame, "unknown", (x, y-20),
                img_font, 2, (255, 0, 0), 2, cv.LINE_AA)

    cv.imshow("face", frame)
    # wait for ESC
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv.destroyAllWindows
