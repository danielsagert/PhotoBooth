import glob
import os
import time

from flask import Flask, render_template
from flask import jsonify
from picamera import PiCamera

from settings import PORT, ROOT_DIRECTORY

app = Flask(__name__)


@app.after_request
def apply_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/api/')
def api_index():
    return jsonify(name='PhotoBooth')

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/photos')
def photos():
    files = glob.glob(ROOT_DIRECTORY + "/photos/*.jpg")
    files.sort(key=os.path.getmtime)
    filenames = [os.path.basename(f) for f in files]
    return jsonify(photos=filenames)


@app.route('/photos/<filename>')
def photo(filename):
    return app.send_static_file('photos/' + filename)


@app.route('/capture')
def capture():
    filename = 'test.jpg'
    with PiCamera() as camera:
        camera.resolution = (1280, 1024)
        # Camera warm-up time
        time.sleep(2)
        camera.capture(ROOT_DIRECTORY + '/photos/' + filename)

    return render_template('photo.html',
                           title='Test photo',
                           filename=filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)
