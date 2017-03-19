from datetime import datetime
from time import sleep

from picamera import PiCamera

from Settings import ROOT_DIRECTORY

lastPhoto = ''


def shoot():
    filename = get_filename()
    print("Capture photo: ", filename)

    with PiCamera() as camera:
        camera.resolution = (1280, 1024)
        # Camera warm-up time
        sleep(2)
        camera.capture(ROOT_DIRECTORY + '/photos/' + filename)

    lastPhoto = filename

    return filename


def get_filename():
    date_and_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return 'photo_' + date_and_time + '.jpg'
