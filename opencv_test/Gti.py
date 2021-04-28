'''
from opencv.org tutorials
https://docs.opencv.org/4.5.2/da/d6e/tutorial_py_geometric_transformations.html

Geometric transformations of images

'''

import numpy as np
import cv2 as cv

# Scaling

img = cv.imread('../foo2.jpg')
res1 = cv.resize(img, None, fx=2, fy=2, interpolation = cv.INTER_CUBIC)

height, width = img.shape[:2]
res2 = cv.resize(img, (2*width, 2*height), interpolation = cv.INTER_CUBIC)


# cv.imshow('img1', res1)
# cv.imshow('img2', res2)
cv.imwrite('img1.jpg', res1) 
cv.imwrite('img2.jpg', res2)
print(res1.shape)


# cv.waitKey(0)
# cv.destroyAllWindows()


# Translation

rows, cols, _ = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow('img', dst)
cv.waitKey(0)
cv.destroyAllWindows()

# Rotation

# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 90, 1)
dst1 = cv.warpAffine(img, M, (cols, rows))

cv.imshow('img1', dst1)
cv.waitKey(0)
cv.destroyAllWindows()

# Affine Transformation
import matplotlib.pyplot as plt

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv.getAffineTransform(pts1, pts2)
dst2 = cv.warpAffine(img, M, (cols, rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst2),plt.title('Output')



# Perspective Transformation
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img, M, (300,300))

plt.figure()
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')


plt.show()

