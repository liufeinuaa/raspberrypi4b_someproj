'''
picamera some test 
i want to close camera led but it doesn't work 

'''


import picamera
from time import sleep

camera = picamera.PiCamera()

camera.led = False # 这里好像没用
# sleep(2)

camera.capture('foo2.jpg')

camera.close()









