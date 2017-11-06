import thread
from time import sleep

import pifacedigitalio as pfio

LED_BUTTON = 0
piface = pfio.PiFaceDigital()
_mode = None
_stop = True


def set_mode(mode):
    global _mode
    _mode = mode


def on():
    thread.start_new_thread(loop, ())


def loop():
    while _stop:
        if _mode == 'fast':
            piface.leds[LED_BUTTON].turn_on()
            sleep(0.5)
            piface.leds[LED_BUTTON].turn_off()
            sleep(0.5)
        elif _mode == 'permanent':
            piface.leds[LED_BUTTON].turn_on()
        else:
            piface.leds[LED_BUTTON].turn_off()
            break


def off():
    global _stop
    _stop = True
