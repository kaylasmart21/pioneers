from picamera import PiCamera
from blinkt import set_pixel, set_brightness, show, clear, set_all
from time import sleep, gmtime, strftime

set_brightness(0.5)
camera=PiCamera()

while True:
    for i in range(8):
              clear()
              set_pixel(i,225, 0, 255)
              show()
              sleep(1)
    clear()
    set_all(0, 255, 0)
    show()
    sleep(2)
    clear()
    output = strftime("/home/pi/Documents/trampoline/image-%d-%m %H:%M:%S.jpg", gmtime())
    camera.capture(output)
    sleep(2)
