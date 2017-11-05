import sys
import threading

import pifacedigitalio as pfio

exit_barrier = threading.Barrier(2)


def button1(event):
    print('Button 1 pressed - capture photo...')


def button2(event):
    print('Button 2 pressed - shutting down...')
    global exit_barrier
    exit_barrier.wait()


piface = pfio.PiFaceDigital()
listener = pfio.InputEventListener(chip=piface)
listener.register(0, pfio.IODIR_FALLING_EDGE, button1)
listener.register(1, pfio.IODIR_FALLING_EDGE, button2)
listener.activate()
print("Button 1 listener activated")

exit_barrier.wait()  # program will wait here until exit_barrier releases
listener.deactivate()
sys.exit()
