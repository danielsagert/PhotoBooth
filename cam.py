import glob
import os
from datetime import datetime
from time import sleep

from PIL import Image, ImageDraw, ImageFont

import led

try:
    from picamera import PiCamera
except ImportError:
    print('picamera not available')
    pass

PHOTO_DIRECTORY = '/var/www/html/photos/'
WIDTH = 1920
HEIGHT = 1080
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
        camera.resolution = (WIDTH, HEIGHT)
        camera.hflip = True
        camera.start_preview()

        overlay = get_overlay('3')
        # camera.add_overlay(overlay.tostring(), layer=3, size=overlay.size, alpha=128, format='rgb')

        # display.countdown(3)
        # Camera warm-up time
        sleep(2)
        led.on('permanent')
        sleep(1)
        print('Capture...')
        camera.hflip = False
        camera.capture(photo_path)
        camera.stop_preview()

    print('Photo captured: ', photo_path)
    led.off()
    ready = True
    return filename


def get_overlay(text):
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 500)
    img = Image.new('RGB', (500, 500))
    draw = ImageDraw.Draw(img)
    text_x, text_y = draw.textsize(text)
    x = (HEIGHT - text_x) / 2
    y = (HEIGHT - text_y) / 2
    draw.text((x, y), text, font=font, fill=(255, 0, 0))
    return img


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
