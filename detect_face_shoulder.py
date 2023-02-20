from __future__ import print_function
import cv2
import argparse
# import numpy as np
# from scipy import stats;

faceCascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_alt.xml')

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Cannot open camera")
    exit()
while True:
    check, frame = cam.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # get all faces in the frame
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('video', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()