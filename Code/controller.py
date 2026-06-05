from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180
camera.resolution = (1920, 1080)


sleep(2)

camera.capture('/home/pi/photo.jpg')
print("Photo prise !")

