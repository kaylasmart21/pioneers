#the first 3 lines of code tell python to use things from python libraries that other people have written. 
#Libraries contain bits of code we can use so we don't have to write lots of code all the time
from picamera import PiCamera
from blinkt import set_pixel, set_brightness, show, clear, set_all
from time import sleep, gmtime, strftime

#blinkt lights can be really bright and hurt your eyes. This controls their brightness
set_brightness(0.5)

#we create 'camera' so we can use it later in our code. 
camera=PiCamera()

#This is a loop. We have this so that it doesnt just take one photo then stop. That would be annoying
while True:
    for i in range(8): #there are 8 lights in blinkt, we go through this 8 times so each light lights up when it's its turn
              clear()
              set_pixel(i,225, 0, 255) #This tells the computer which light, how much red, how much green and how much blue
              show()
              sleep(1)
    clear()
    set_all(0, 255, 0) #puts all the light on in green
    show()
    sleep(2)
    clear()
    output = strftime("/home/pi/Documents/trampoline/image-%d-%m %H:%M:%S.jpg", gmtime()) #we create 'output' and which is the place the image is stored and it's name. It's name contains the time. This means we don't keep overwriting our images
    camera.capture(output) #This takes a photograph and saves it to the place we told it too in 'output'
    sleep(2)
