from time import sleep

import pifacedigitalio as pfio

piface = pfio.PiFaceDigital()
_mode = None
_stop = True


def set_mode(mode):
    global _mode
    _mode = mode


def on():
    while _stop:
        if _mode == 'fast':
            piface.leds[0].turn_on()
            sleep(0.5)
            piface.leds[0].turn_off()
            sleep(0.5)
        elif _mode == 'permanent':
            piface.leds[0].turn_on()


def off():
    global _stop
    _stop = True
