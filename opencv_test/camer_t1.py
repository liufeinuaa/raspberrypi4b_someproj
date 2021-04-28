import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile('/home/pi/PythonProjects/image2.jpg'))

if img is None:
    sys.exit('could not read the image')

cv.imshow("display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite('image3.png', img)






