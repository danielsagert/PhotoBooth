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
from settings import MAX_PHOTOS


def shoot():
    filename = get_filename()

    with PiCamera() as camera:
        camera.resolution = (1280, 1024)
        # Camera warm-up time
        sleep(2)
        photos_path = ROOT_DIRECTORY + '/photos/' + filename
        camera.capture(photos_path)
        print('Photo captured: ', photos_path)

    return filename


def get_filename():
    date_and_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return 'photo_' + date_and_time + '.jpg'


def get_photos():
    files = glob.glob(ROOT_DIRECTORY + '/photos/*.jpg')
    files.sort(key=os.path.getmtime, reverse=True)
    del files[MAX_PHOTOS:]
    filenames = [os.path.basename(f) for f in files]
    return filenames


def get_last_photo():
    filenames = get_photos()
    if len(filenames) > 0: return filenames[0]
    return ''
