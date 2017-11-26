import os

from PIL import Image

from logger import log
from settings import PHOTO_DIRECTORY, THUMBNAIL_DIRECTORY


def get_thumbnail_path(filename):
    path_original = PHOTO_DIRECTORY + filename
    path_thumbnail = THUMBNAIL_DIRECTORY + filename

    if not os.path.isfile(path_thumbnail):
        log('Start image resizing: ' + filename)
        width = 300
        image = Image.open(path_original)
        width_percent = (width / float(image.size[0]))
        height = int((float(image.size[1]) * float(width_percent)))
        image = image.resize((width, height), Image.ANTIALIAS)
        image.save(path_thumbnail, 'JPEG')

    return path_thumbnail
