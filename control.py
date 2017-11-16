import sys
import thread
import time

import pifacedigitalio as pfio

import cam

shutdown = False


def button1_pressed(event):
    print('Button 1 pressed - capture photo...')
    thread.start_new_thread(cam.shoot, ())


def button2_pressed(event):
    print('Button 2 pressed - trigger shutdown...')
    global shutdown
    shutdown = True


def monitor_buttons():
    piface = pfio.PiFaceDigital()
    listener = pfio.InputEventListener(chip=piface)
    listener.register(0, pfio.IODIR_FALLING_EDGE, button1_pressed)
    listener.register(1, pfio.IODIR_FALLING_EDGE, button2_pressed)
    listener.activate()
    print("Button 1 listener activated")

    while not shutdown:
        time.sleep(1)

    listener.deactivate()
    print('Control interface shut down')
    sys.exit()


if __name__ == "__main__":
    monitor_buttons()
