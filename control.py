import sys
import thread
import time

import pifacedigitalio as pfio

import cam

shutdown = False


def button1(event):
    print('Button 1 pressed - capture photo...')
    thread.start_new_thread(cam.shoot(), ())


def button2(event):
    print('Button 2 pressed - trigger shutdown...')
    global shutdown
    shutdown = True


piface = pfio.PiFaceDigital()
listener = pfio.InputEventListener(chip=piface)
listener.register(0, pfio.IODIR_FALLING_EDGE, button1)
listener.register(1, pfio.IODIR_FALLING_EDGE, button2)
listener.activate()
print("Button 1 listener activated")

while not shutdown:
    time.sleep(1)

listener.deactivate()
print('Control interface shut down')
sys.exit()
