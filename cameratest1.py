import picamera
from time import sleep

camera = picamera.PiCamera()

try:
    camera.resolution = (1024, 768)
    camera.rotation = 180
    camera.brightness = 50
    camera.start_preview()

    camera.annotate_text = 'from Raspberry Pi'
    sleep(3)

    camera.capture('test2.jpg')

finally:
    camera.stop_preview()
    camera.close()






