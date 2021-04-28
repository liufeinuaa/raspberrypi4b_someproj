'''
from opencv.org tutorials
https://docs.opencv.org/4.5.2/dc/da5/tutorial_py_drawing_functions.html

Drawing funciton in opencv

'''


import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512, 512, 3),  np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# Drawing Rectangle
cv.rectangle(img, (348, 0), (510, 128), (0, 255, 0), 3)

# Drawing Circle
cv.circle(img, (447, 63), 63, (0,0,225), -1)

# Drawing Ellipse
# cv.ellipse(img, (256, 256), (100, 50), 0, 0,180, 255, -1)
cv.ellipse(img, (256, 256), (100, 50), 0, 0,180, (0, 255, 0), -1)

# Drawing Polygon
pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
pts = pts.reshape((-1,1,2))
# cv.polylines(img, [pts], True, (0,225,255))
cv.polylines(img, [pts], False, (0,225,255))


font = cv.FONT_HERSHEY_SIMPLEX
# cv.putText(img, 'OpenCV', (10,500), font, 4, (255, 255, 255), 2, cv.LINE_AA)
cv.putText(img, 'fucking the word', (10,500), font, 1, (255, 255, 255), 2, cv.LINE_AA)





# 辅助保存图片代码
cv.imshow("draw img window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite('image5.jpg', img)
    cv.destoryAllWindows()
elif k == ord('q'):
    cv.destoryAllWindows()







