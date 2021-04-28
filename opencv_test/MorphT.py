'''
from opencv.org tutorials
https://docs.opencv.org/4.5.2/d9/d61/tutorial_py_morphological_ops.html

Morphological Transformations

'''

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 1. Erosion 腐蚀

img = cv.imread('../j.png', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(img, kernel, iterations=1)

# cv.imshow('res', erosion)
# k = cv.waitKey(0)
# cv.destoryAllWindows()

plt.subplot(121)
plt.imshow(img, 'gray')
plt.subplot(122)
plt.imshow(erosion, 'gray')
plt.show()

# 2. Dilation 膨胀
dilation = cv.dilate(img, kernel, iterations=1)

plt.subplot(121)
plt.imshow(img, 'gray')
plt.subplot(122)
plt.imshow(dilation, 'gray')
plt.show()

# 3. Opening
img = cv.imread('../opening.png')
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
ero = cv.erode(img, kernel, iterations=1)
res = cv.dilate(ero, kernel, iterations=1)


plt.subplot(141)
plt.imshow(img, 'gray')
plt.subplot(142)
plt.imshow(res, 'gray')
plt.subplot(143)
plt.imshow(opening, 'gray')
plt.subplot(144)
plt.imshow(ero, 'gray')
plt.show()



# 4. Closing
img = cv.imread('../closing.png')
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
dil = cv.dilate(img, kernel, iterations=1)
res = cv.erode(dil, kernel, iterations=1)


plt.subplot(141)
plt.imshow(img, 'gray')
plt.subplot(142)
plt.imshow(res, 'gray')
plt.subplot(143)
plt.imshow(closing, 'gray')
plt.subplot(144)
plt.imshow(dil, 'gray')
plt.show()


# 5. Morphological Gradient
img = cv.imread('../j.png', 0)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

plt.subplot(121)
plt.imshow(img, 'gray')
plt.subplot(122)
plt.imshow(gradient, 'gray')
plt.show()


# 6. Top Hat
kernel = np.ones((9,9), np.uint8)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)

plt.subplot(121)
plt.imshow(img, 'gray')
plt.subplot(122)
plt.imshow(tophat, 'gray')
plt.show()

# 7. Black Hat
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

plt.subplot(121)
plt.imshow(img, 'gray')
plt.subplot(122)
plt.imshow(blackhat, 'gray')
plt.show()

# Structuring Element
# Rectangular Kernel
print(cv.getStructuringElement(cv.MORPH_RECT, (5, 5)))
print('\n')
# Elliptical Kernel
print(cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5)))
print('\n')
# Cross-shaped Kernel
print(cv.getStructuringElement(cv.MORPH_CROSS, (5, 5)))

