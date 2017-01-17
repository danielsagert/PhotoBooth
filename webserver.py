from flask import Flask, render_template
from flask import jsonify, url_for
from picamera import PiCamera

import settings

app = Flask(__name__)

@app.route('/api/')
def api_index():
    return jsonify(result='PhotoBooth')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/photo')
def photo():
    with PiCamera() as camera:
        camera.capture('/home/pi/PhotoBooth/static/photos/test.jpg')

    return render_template('photo.html',
                           title='Test photo',
                           photo_url=url_for('static', filename='test.jpg'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=settings.PORT)
