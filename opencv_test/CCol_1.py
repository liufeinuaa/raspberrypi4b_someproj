'''
from opencv.org tutorials
https://docs.opencv.org/4.5.2/df/d9d/tutorial_py_colorspaces.html

Changing Colorspaces

'''


# import cv2 as cv
# flags = [i for i in dir(cv) if i.startswith('COLOR_')]
# print(flags) 


# Object Tracking

import cv2 as cv
import numpy as np 

cap = cv.VideoCapture(0)

while(1):
    # Take each frame
    rat, frame = cap.read()
    frame = cv.flip(frame, 0)

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # lower_red = np.array([0,0,10]) # 这里失败的原因是这里的数组的值应该是HSV空间中的而不是BGR
    # upper_rad = np.array([50,50,100])
    # mask = cv.inRange(hsv, lower_red, upper_rad)

    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # lower_green = np.array([50,50,50])
    # upper_green = np.array([70,255,255])
    # mask = cv.inRange(hsv, lower_green, upper_green)


    # lower_red = np.array([0,100,100])
    # upper_red = np.array([20,255,255])
    # mask = cv.inRange(hsv, lower_red, upper_red)


    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5)
    if k == ord('q'):
        break

cv.destroyAllWindows()








