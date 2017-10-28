import glob
import os
from datetime import datetime
from time import sleep

try:
    from picamera import PiCamera
except ImportError:
    print('picamera not available')
    pass

from settings import ROOT_DIRECTORY


def shoot():
    filename = get_filename()

    with PiCamera() as camera:
        camera.resolution = (1280, 1024)
        # Camera warm-up time
        sleep(2)
        photos_path = ROOT_DIRECTORY + '/static/photos/' + filename
        camera.capture(photos_path)
        print('Photo captured: ', photos_path)

    return filename


def get_filename():
    date_and_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return 'photo_' + date_and_time + '.jpg'


def get_photos(last_photo):
    if last_photo is None:
        print('Get all photos')
    else:
        print ('Get all photos until: ', last_photo)

    # Get all JPGs from the photo directory and sort them by timestamp descending
    files = glob.glob(ROOT_DIRECTORY + '/static/photos/*.jpg')
    files.sort(key=os.path.getmtime, reverse=True)

    # Keep only the last 15 photos
    del files[15:]

    # Get all filenames until all new photos are collected
    filenames = []
    for f in files:
        filename = os.path.basename(f)

        if filename == last_photo:
            break

        filenames.append(filename)

    print('Found ', len(filenames), ' new photo(s): ', filenames)
    return filenames


def get_last_photo():
    print('Get last photo')
    files = glob.glob(ROOT_DIRECTORY + '/static/photos/*.jpg')

    if len(files) < 1:
        return ''

    files.sort(key=os.path.getmtime, reverse=True)
    latest_file = files[0]
    filename = os.path.basename(latest_file)
    return filename
