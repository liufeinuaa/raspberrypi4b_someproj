'''
from opencv.org tutorials
https://docs.opencv.org/4.5.2/d3/df2/tutorial_py_basic_ops.html

Basic Operations on images

'''

import numpy as np
import cv2 as cv

img = cv.imread('image2.jpg')

# Accessing and Modifying pixel values
px = img[100,100]
print(px)

blue = img[100,100,0]
print( blue )

print(img.item(10,10,2))
img.itemset((10,10,2),100)
print(img.item(10,10,2))

# Accessing Image Properties
print( img.shape )
print( img.size )
print( img.dtype )

# Image ROI
face = img[390:680, 530:740]
cv.imshow("display window", face)
img2 = img
img2[90:380, 130:340] = face
cv.imshow("display window2", img2)


b,g,r = cv.split(img)
img3 = cv.merge((b,g,r))
img3[:,:,2] = 0
cv.imshow("display window3", img3)


# Making Borders for Images (Padding)

from matplotlib import pyplot as plt 

BLUE = [255,0,0]
img1 = cv.imread('image3.png')
# img1 = img

replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()

k = cv.waitKey(0)
if k == ord("q"):
    cv.destoryAllWindows()