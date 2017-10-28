from flask import Flask, jsonify, request

from cam import shoot, get_photos, get_last_photo

app = Flask(__name__)


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
    last_photo = request.args.get('lastphoto')
    filenames = get_photos(last_photo)
    return jsonify(filenames=filenames)


@app.route('/photos/last')
def new_photo():
    filename = get_last_photo()
    return jsonify(filename=filename)


if __name__ == "__main__":
    app.run()
