import os
import sys
import thread
import time

import pifacedigitalio as pfio

import cam
from logger import log

shutdown = False


def button1_pressed(event):
    log('Button 1 pressed - capture photo...')
    thread.start_new_thread(cam.shoot, ())


def button2_pressed(event):
    log('Button 2 pressed - shutdown application...')
    global shutdown
    shutdown = True


def button3_pressed(event):
    log('Button 3 pressed - reboot system...')
    os.system('reboot')


def button4_pressed(event):
    log('Button 4 pressed - shutdown system...')
    os.system('shutdown -h now')


def monitor_buttons():
    piface = pfio.PiFaceDigital()
    listener = pfio.InputEventListener(chip=piface)
    listener.register(0, pfio.IODIR_FALLING_EDGE, button1_pressed)
    listener.register(1, pfio.IODIR_FALLING_EDGE, button2_pressed)
    listener.register(2, pfio.IODIR_FALLING_EDGE, button3_pressed)
    listener.register(3, pfio.IODIR_FALLING_EDGE, button4_pressed)
    listener.activate()
    log("Button listeners activated")

    while not shutdown:
        time.sleep(1)

    listener.deactivate()
    log('Control interface shut down')
    sys.exit()


if __name__ == "__main__":
    monitor_buttons()
