'''
from opencv.org tutorials
https://docs.opencv.org/4.5.2/db/d5b/tutorial_py_mouse_handling.html

Mouse as a Paint-Brush

这个对我不太有用，随便试试
'''


# To list all available events available，查看可用的opencv中可用的事件
# import cv2 as cv
# events = [i for i in dir(cv) if 'EVENT' in i]
# print( events )


# import numpy as np
# import cv2 as cv
# # mouse callback function
# def draw_circle(event,x,y,flags,param):
#     if event == cv.EVENT_LBUTTONDBLCLK:
#         cv.circle(img,(x,y),100,(255,0,0),-1)
# # Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
# cv.namedWindow('image')
# cv.setMouseCallback('image',draw_circle)

# # while(1): # 这行不好使，无法推出程序
# #     cv.imshow('image',img)
# #     if cv.waitKey(20) & 0xFF == 27:
# #         break

# while(1):
#     cv.imshow('image',img)
#     if cv.waitKey(20) == ord('q'):
#         break
# cv.destroyAllWindows()



import numpy as np
import cv2 as cv
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)


img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
# while(1):
#     cv.imshow('image',img)
#     k = cv.waitKey(1) & 0xFF
#     if k == ord('m'):
#         mode = not mode
#     elif k == 27: # 这里好像不好使，不知道意思，也没用
#         break
# cv.destroyAllWindows()

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == ord('q'): # 这里好像不好使，不知道意思，也没用
        break
cv.destroyAllWindows()
