import glob
import os
from datetime import datetime
from time import sleep

import led

try:
    from picamera import PiCamera
except ImportError:
    print('picamera not available')
    pass

PHOTO_DIRECTORY = '/var/www/html/photos/'
ready = True


def shoot():
    global ready

    if not ready:
        print('Camera is not ready yet')
        return

    ready = False
    led.on('fast')

    if not os.path.exists(PHOTO_DIRECTORY):
        os.makedirs(PHOTO_DIRECTORY)

    filename = get_filename()
    photo_path = PHOTO_DIRECTORY + filename

    with PiCamera() as camera:
        camera.resolution = (2592, 1944)
        camera.start_preview()
        # camera.start_preview(alpha=200)

        # img = Image.open('static/photos/photobooth-test.jpg')
        # pad = Image.new('RGB', (
        #     ((img.size[0] + 31) // 32) * 32,
        #     ((img.size[1] + 15) // 16) * 16,
        # ))
        # pad.paste(img, (0, 0))
        # camera.add_overlay(pad.tostring(), layer=3, size=img.size, alpha=3)
        # o.alpha = 128
        # o.layer = 3

        # text = '3'
        # img = Image.new("RGB", (1024, 768))
        # draw = ImageDraw.Draw(img)
        # draw.font = ImageFont.truetype(
        #     "/usr/share/fonts/truetype/freefont/FreeSerif.ttf",
        #     50)
        # draw.text((10, 10), text, (255, 255, 255))
        # camera.add_overlay(img.tostring(), layer=3, size=img.size, alpha=128)

        # display.countdown(3)
        # Camera warm-up time
        sleep(2)
        led.on('permanent')
        sleep(1)
        print('Capture...')
        camera.capture(photo_path)
        camera.stop_preview()

    print('Photo captured: ', photo_path)
    led.off()
    ready = True
    return filename


def get_filename():
    date_and_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return 'photo_' + date_and_time + '.jpg'


def get_filenames(last_filename):
    if last_filename is None:
        print('Get all filenames')
    else:
        print ('Get all filenames until: ', last_filename)

    # Get all JPGs from the photo directory and sort them by timestamp descending
    files = glob.glob(PHOTO_DIRECTORY + '*.jpg')
    files.sort(key=os.path.getmtime, reverse=True)

    # Keep only the last 15 files
    del files[15:]

    # Get all filenames until all new files are collected
    filenames = []
    for f in files:
        filename = os.path.basename(f)

        if filename == last_filename:
            break

        filenames.append(filename)

    print('Found ', len(filenames), ' new file(s): ', filenames)
    return filenames


def get_last_filename():
    files = glob.glob(PHOTO_DIRECTORY + '*.jpg')

    if len(files) < 1:
        return ''

    files.sort(key=os.path.getmtime, reverse=True)
    latest_file = files[0]
    filename = os.path.basename(latest_file)
    return filename
