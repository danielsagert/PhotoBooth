import flask

import cam

app = flask.Flask(__name__)


@app.after_request
def apply_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/')
def flashback():
    return app.send_static_file('flashback.html')


@app.route('/summary')
def summary():
    return app.send_static_file('summary.html')


@app.route('/capture')
def capture():
    filename = cam.shoot()
    return flask.jsonify(filename=filename)


@app.route('/photos')
def photos():
    limit = flask.request.args.get('limit')
    filenames = cam.get_filenames(limit)
    return flask.jsonify(filenames=filenames)


@app.route('/photos/<filename>')
def photo(filename):
    return app.send_static_file('photos/' + filename)


if __name__ == "__main__":
    app.run()
