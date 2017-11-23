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

PHOTO_DIRECTORY = '/home/pi/PhotoBooth/static/photos/'
PHOTO_WIDTH = 2592
PHOTO_HEIGHT = 1944
PREVIEW_WIDTH = 1280
PREVIEW_HEIGHT = 1024
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

    filename = generate_filename()
    photo_path = PHOTO_DIRECTORY + filename

    with PiCamera() as camera:
        camera.resolution = (PREVIEW_WIDTH, PREVIEW_HEIGHT)
        camera.hflip = True
        camera.start_preview()

        overlay = None

        for i in range(3, 0, -1):
            if overlay:
                camera.remove_overlay(overlay)

            overlay_img = get_overlay(str(i))
            overlay = camera.add_overlay(overlay_img.tostring(), layer=3, size=overlay_img.size, alpha=128,
                                         format='rgb')
            sleep(1)

        print('Capture...')

        led.on('permanent')
        camera.remove_overlay(overlay)
        overlay_img = get_overlay('Smile!')
        overlay = camera.add_overlay(overlay_img.tostring(), layer=3, size=overlay_img.size, alpha=128, format='rgb')
        sleep(1)

        camera.remove_overlay(overlay)
        camera.stop_preview()
        camera.hflip = False
        camera.resolution = (PHOTO_WIDTH, PHOTO_HEIGHT)
        camera.capture(photo_path)

    print('Photo captured: ', photo_path)
    led.off()
    ready = True
    return filename


def get_overlay(text):
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 400)
    img = Image.new('RGB', (PREVIEW_WIDTH, PREVIEW_HEIGHT))
    draw = ImageDraw.Draw(img)
    text_x, text_y = draw.textsize(text, font)
    x = (PREVIEW_WIDTH - text_x) / 2
    y = (PREVIEW_HEIGHT - text_y) / 2
    draw.text((x, y), text, font=font, fill=(255, 0, 0))
    return img


def generate_filename():
    date_and_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return 'photo_' + date_and_time + '.jpg'


def get_filenames(limit):
    # Get all JPGs from the photo directory and sort them by timestamp descending
    files = glob.glob(PHOTO_DIRECTORY + '*.jpg')
    files.sort(key=os.path.getmtime, reverse=True)

    # Remove file which are not completely written yet (size 0)
    files = list(filter(lambda x: os.stat(x).st_size > 0, files))

    # Keep only the last x files
    if limit is not None:
        del files[int(limit):]

    # Get all filenames until all new files are collected
    filenames = []
    for f in files:
        filenames.append(os.path.basename(f))

    return filenames
