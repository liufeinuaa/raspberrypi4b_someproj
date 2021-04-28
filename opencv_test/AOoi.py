'''
from opencv.org tutorials
https://docs.opencv.org/4.5.2/d3/df2/tutorial_py_basic_ops.html

Arithmetic Operations on images
图像上的算数运算

'''

import numpy as np
import cv2 as cv

img1 = cv.imread("../test1.jpg")
img2 = cv.imread("../test2.jpg")

# Image Blending 图像融合或虚化
dst = cv.addWeighted(img1, 0.7, img2, 0.3, 0)

cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()

# Bitwise Operations 按位运算
img3 = cv.imread('image4.jpg')
rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img3, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
cv.imshow("gray", img2gray)
cv.imshow("mask", mask)
cv.imshow("mask_inv", mask_inv)

# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
cv.imshow("black-out", img1_bg)
# Take only region of logo from logo image.
img3_fg = cv.bitwise_and(img3, img3, mask=mask)
cv.imshow("fg", img3_fg)

# Put logo in ROI and modify the main image
dst1 = cv.add(img1_bg, img3_fg)
cv.imshow("dst1", dst1)
img1[0:rows, 0:cols] = dst1
cv.imshow('res', img1)


cv.waitKey(0)
cv.destroyAllWindows()