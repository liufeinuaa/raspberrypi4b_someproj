'''
from opencv.org tutorials
https://docs.opencv.org/4.5.2/d4/d13/tutorial_py_filtering.html

Smoothing Images

'''

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../filter.jpg')
img1 = cv.imread('../median.jpg')
img2 = cv.imread('../bilateral.jpg')

# 2D Convolution ( Image Filtering )
# kernel = np.ones((5,5), np.float32)/25
# dst = cv.filter2D(img, -1, kernel)

# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()


# Image Blurring (Image Smoothing)
# 1. Averaging
# blur = cv.blur(img, (5, 5))

# 2. Gaussian Blurring
# blur = cv.GaussianBlur(img1,(5,5),0)

# plt.subplot(121),plt.imshow(img1),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
# plt.xticks([]), plt.yticks([])
# plt.show()

# 3. Median Blurring
# median = cv.medianBlur(img1, 5)

# plt.subplot(121),plt.imshow(img1),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(median),plt.title('Blurred')
# plt.xticks([]), plt.yticks([])
# plt.show()



# 4. Bilateral Filtering
blur = cv.bilateralFilter(img2, 9, 75, 75)

plt.subplot(121),plt.imshow(img2),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
