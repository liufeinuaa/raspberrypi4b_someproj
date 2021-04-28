'''
from opencv.org tutorials
https://docs.opencv.org/4.5.2/df/d9d/tutorial_py_colorspaces.html

Changing Colorspaces

'''

import cv2 as cv
import numpy as np


# How to find HSV values to track?

green = np.uint8([[[0,255,0]]])
red = np.uint8([[[0,0,255]]])
blue = np.uint8([[[255,0,0]]])

hsv_green = cv.cvtColor(green, cv.COLOR_BGR2HSV)
hsv_red = cv.cvtColor(red, cv.COLOR_BGR2HSV)
hsv_blue = cv.cvtColor(blue, cv.COLOR_BGR2HSV)

# print()
print('green hsv value: ', hsv_green)
print('red hsv value: ', hsv_red)
print('blue hsv value: ', hsv_blue)







