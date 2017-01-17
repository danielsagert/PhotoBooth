from flask import Flask, render_template
from flask import jsonify
from picamera import PiCamera

import settings

app = Flask(__name__)
cam = PiCamera()

@app.route('/api/')
def api_index():
    return jsonify(result='PhotoBooth')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/photo')
def photo():
    cam.capture('/home/pi/PhotoBooth/static/photos')
    return render_template('photo.html',
                           title='Last photo',
                           text='Not implemented yet')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=settings.PORT)
