from threading import Thread
from time import sleep

import pifacedigitalio as pfio

LED_BUTTON = 0
piface = pfio.PiFaceDigital()
_mode = None
_stop = True
_thread = None


def on(mode):
    global _thread
    global _stop
    global _mode

    _mode = mode
    _stop = False

    if _thread is None or not _thread.is_alive():
        _thread = Thread(target=loop, args=())
        _thread.start()


def loop():
    while not _stop:
        if _mode == 'fast':
            piface.leds[LED_BUTTON].turn_on()
            sleep(0.2)
            piface.leds[LED_BUTTON].turn_off()
            sleep(0.2)
        elif _mode == 'permanent':
            piface.leds[LED_BUTTON].turn_on()
        else:
            break

    piface.leds[LED_BUTTON].turn_off()


def off():
    global _stop
    _stop = True
