from io import BytesIO

from PIL import Image

from logger import log
from settings import PHOTO_DIRECTORY


def resize_image(filename):
    log('Start image resizing: ' + filename)
    width = 300
    image = Image.open(PHOTO_DIRECTORY + filename)
    width_percent = (width / float(image.size[0]))
    height = int((float(image.size[1]) * float(width_percent)))
    image = image.resize((width, height), Image.ANTIALIAS)

    log('Image resizing: ' + filename)

    byte_io = BytesIO()
    image.save(byte_io, "JPEG", quality=80, optimize=True, progressive=True)
    byte_io.seek(0)
    return byte_io
