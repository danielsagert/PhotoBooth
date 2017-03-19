from flask import Flask, send_from_directory
from flask import jsonify

from PhotoBooth import shoot, get_photos, get_last_photo
from Settings import PORT

app = Flask(__name__)


def start():
    app.run(host='0.0.0.0', port=PORT, debug=True)


@app.after_request
def apply_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/')
def index():
    print('Deliver index page')

    return app.send_static_file('index.html')


@app.route('/capture')
def capture():
    filename = shoot()
    return jsonify(filename=filename)


@app.route('/photos')
def photos():
    print('Deliver filenames all photos')
    filenames = get_photos()
    return jsonify(photos=filenames)


@app.route('/photos/<filename>')
def photo(filename):
    print('Deliver photo: ', filename)
    return send_from_directory('photos', filename)


@app.route('/photos/last')
def new_photo():
    filename = get_last_photo
    return jsonify(filename=filename)
