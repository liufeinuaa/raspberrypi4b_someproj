import picamera
from time import sleep


# camera = picamera.PiCamera()

# try:
#     camera.resolution = (1024, 768)
#     camera.rotation = 180
#     camera.brightness = 60
#     camera.start_preview()

#     camera.annotate_text = 'from Raspberry Pi'
#     sleep(3)

#     camera.capture('image2.jpg')

# finally:
#     camera.stop_preview()
#     camera.close()


with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.rotation = 180
    camera.start_preview()
    camera.start_recording('video2.h264')
    camera.wait_recording(10)
    camera.stop_recording()
    camera.close()
