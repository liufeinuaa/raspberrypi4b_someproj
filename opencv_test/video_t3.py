'''
from opencv.org tutorials
https://docs.opencv.org/4.5.2/dd/d43/tutorial_py_video_display.html

Gettting started with videos

- playing video from file 
'''



import numpy as np
import cv2 as cv

cap = cv.VideoCapture('output.avi')

while cap.isOpened():
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("can't receive frame (stream end?). exiting...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()





