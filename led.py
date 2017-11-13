import threading
from time import sleep

import pifacedigitalio as pfio

BUTTON = 0
piface = pfio.PiFaceDigital()
_mode = 'fast'
_thread = None
_event = None


def on(mode):
    global _mode
    global _thread
    global _event

    _mode = mode

    if _thread is None or _event.isSet():
        _event = threading.Event()
        _thread = threading.Thread(name='flash', target=flash, args=(_event))
        _thread.start()


def flash(event):
    while not event.isSet():
        if _mode == 'fast':
            piface.leds[BUTTON].turn_on()
            sleep(0.2)
            piface.leds[BUTTON].turn_off()
            sleep(0.2)
        elif _mode == 'permanent':
            piface.leds[BUTTON].turn_on()
        else:
            break

    piface.leds[BUTTON].turn_off()


def off():
    global _event
    _event.set()
