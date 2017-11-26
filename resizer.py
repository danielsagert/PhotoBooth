import os

from PIL import Image

from logger import log
from settings import PHOTO_DIRECTORY


def resize_image(filename):
    path_original = PHOTO_DIRECTORY + filename
    path_resized = PHOTO_DIRECTORY + '/resized/' + filename

    if not os.path.isfile(path_resized):
        log('Start image resizing: ' + filename)
        width = 300
        image = Image.open(path_original)
        width_percent = (width / float(image.size[0]))
        height = int((float(image.size[1]) * float(width_percent)))
        image = image.resize((width, height), Image.ANTIALIAS)
        image.save(path_resized, 'JPEG')

    return path_resized
