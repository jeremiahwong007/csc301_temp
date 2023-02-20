from __future__ import print_function

import cv2
import argparse
# import numpy as np
# from scipy import stats;

faceCascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_alt.xml')

# Helper function to write raw data to output file
def write_data_raw(x: int, y: int, w: int, h: int, file) -> bool:
    file.write("(" + str(x) + ", " + str(y) + ")" + " " 
                + "(" + str(x + w) + ", " + str(y + h) + ")\n")

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Cannot open camera")
    exit()

file = open("raw.txt", "w")
file.write("(x, y) (x + w, x + h)\n")

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
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Write data to file
        write_data_raw(x, y, w, h, file)

    cv2.imshow('video', frame)

    # esc key
    key = cv2.waitKey(1)
    if key == 27:
        break

file.close()
cam.release()
cv2.destroyAllWindows()