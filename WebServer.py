import glob
import os

from flask import Flask, send_from_directory
from flask import jsonify
from flask_socketio import SocketIO, send

from PhotoBooth import shoot
from Settings import ROOT_DIRECTORY

app = Flask(__name__)
socketio = SocketIO(app)


def start():
    socketio.run(app, host='0.0.0.0')


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
    send('capture')
    return jsonify(filename=filename)


@app.route('/photos')
def photos():
    print('Deliver filenames all photos')

    files = glob.glob(ROOT_DIRECTORY + '/photos/*.jpg')
    files.sort(key=os.path.getmtime, reverse=True)
    filenames = [os.path.basename(f) for f in files]
    return jsonify(photos=filenames)


@app.route('/photos/<filename>')
def photo(filename):
    print('Deliver photo: ', filename)

    return send_from_directory('photos', filename)