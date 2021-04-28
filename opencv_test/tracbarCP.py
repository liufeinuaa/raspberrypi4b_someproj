'''
from opencv.org tutorials
https://docs.opencv.org/4.5.2/d9/dc8/tutorial_py_trackbar.htm

Trackbar as the color Palette

这个对我不太有用，随便试试
'''

import numpy as np
import cv2 as cv

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')

# Create a black image, a window
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)

# create switch for ON/OFF functionality
switch = '0: OFF \n 1: ON' 
cv.createTrackbar(switch, 'image', 0, 1, nothing)


while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1)
    if k == ord('q'):
        break
    
    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv.destoryAllWindows()