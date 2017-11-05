import glob
import os
from datetime import datetime
from time import sleep

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

    if not os.path.exists(PHOTO_DIRECTORY):
        os.makedirs(PHOTO_DIRECTORY)

    filename = get_filename()
    photo_path = PHOTO_DIRECTORY + filename

    with PiCamera() as camera:
        camera.resolution = (1280, 1024)
        camera.start_preview()
        # Camera warm-up time
        sleep(2)
        camera.capture(photo_path)
        camera.stop_preview()

    print('Photo captured: ', photo_path)
    ready = True
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
    files = glob.glob(PHOTO_DIRECTORY + '*.jpg')
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
    files = glob.glob(PHOTO_DIRECTORY + '*.jpg')

    if len(files) < 1:
        return ''

    files.sort(key=os.path.getmtime, reverse=True)
    latest_file = files[0]
    filename = os.path.basename(latest_file)
    return filename
