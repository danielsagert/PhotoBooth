import time

from flask import Flask, render_template
from flask import jsonify
from picamera import PiCamera

import settings

app = Flask(__name__)

@app.route('/api/')
def api_index():
    return jsonify(result='PhotoBooth')

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/photo/<filename>')
def photo(filename):
    return app.send_static_file('photos/' + filename)


@app.route('/capture')
def capture():
    filename = 'test.jpg'
    with PiCamera() as camera:
        camera.resolution = (1280, 1024)
        # Camera warm-up time
        time.sleep(2)
        camera.capture('/home/pi/PhotoBooth/static/photos/' + filename)

    return render_template('photo.html',
                           title='Test photo',
                           filename=filename)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=settings.PORT)
