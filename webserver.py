import flask

import cam

app = flask.Flask(__name__)


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
    filename = cam.shoot()
    return flask.jsonify(filename=filename)


@app.route('/photos')
def photos():
    filenames = cam.get_filenames()
    return flask.jsonify(filenames=filenames)


if __name__ == "__main__":
    app.run()
