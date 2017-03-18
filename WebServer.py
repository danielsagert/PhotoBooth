import glob
import os

from flask import Flask, send_from_directory
from flask import jsonify
from flask_socketio import SocketIO, emit

from PhotoBooth import shoot
from Settings import PORT, ROOT_DIRECTORY

app = Flask(__name__)
socketio = SocketIO(app)


def start():
    app.run(debug=True, host='0.0.0.0', port=PORT)
    socketio.run(app)


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

    files = glob.glob(ROOT_DIRECTORY + '/photos/*.jpg')
    files.sort(key=os.path.getmtime, reverse=True)
    filenames = [os.path.basename(f) for f in files]
    return jsonify(photos=filenames)


@app.route('/photos/<filename>')
def photo(filename):
    print('Deliver photo: ', filename)

    return send_from_directory('photos', filename)


@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})


@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)


@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')
