import sys

import pifacedigitalio as pfio

listener = None


def button1(event):
    print('Button 1 pressed - capture photo...')


def button2(event):
    print('Button 2 pressed - shutting down...')
    global listener
    listener.deactivate()
    sys.exit()


piface = pfio.PiFaceDigital()
listener = pfio.InputEventListener(chip=piface)
listener.register(0, pfio.IODIR_FALLING_EDGE, button1)
listener.register(1, pfio.IODIR_FALLING_EDGE, button2)
listener.activate()
print("Button 1 listener activated")
