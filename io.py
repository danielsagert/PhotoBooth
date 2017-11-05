import pifacedigitalio


def button1(event):
    print('Button 1 pressed - capture photo...')


def button2(event):
    print('Button 2 pressed - shutting down...')
    listener.deactivate()


piface = pifacedigitalio.PiFaceDigital()
listener = pifacedigitalio.InputEventListener(chip=piface)
listener.register(0, pifacedigitalio.IODIR_FALLING_EDGE, button1)
listener.register(1, pifacedigitalio.IODIR_FALLING_EDGE, button2)
listener.activate()
print("Button 1 listener activated")
