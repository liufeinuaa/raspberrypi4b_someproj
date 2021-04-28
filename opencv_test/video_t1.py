'''
from opencv.org tutorials
https://docs.opencv.org/4.5.2/dd/d43/tutorial_py_video_display.html

Gettting started with videos

- capture video from camera
'''






import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print('cannot open camera')
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("can't receive frame (stream end?). exiting..")
        break

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destoryAllWindows()



    




