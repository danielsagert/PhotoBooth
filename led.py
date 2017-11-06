import thread
from time import sleep

import pifacedigitalio as pfio

LED_BUTTON = 0
piface = pfio.PiFaceDigital()
_active = False
_mode = None
_stop = True


def on(mode):
    global _active
    global _stop
    global _mode

    _mode = mode

    if not _active:
        _active = True
        _stop = False
        thread.start_new_thread(loop, ())


def loop():
    global _active

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

    _active = False


def off():
    global _stop
    _stop = True
    piface.leds[LED_BUTTON].turn_off()
