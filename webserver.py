import flask

import cam
import resizer

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


@app.route('/photos')
def photos():
    limit = flask.request.args.get('limit')
    filenames = cam.get_filenames(limit)
    return flask.jsonify(filenames=filenames)


@app.route('/photos/<filename>')
def photo(filename):
    return app.send_static_file('photos/' + filename)


@app.route('/photos/thumbnail/<filename>')
def thumbnail(filename):
    resizer.create_thumbnail(filename)
    return app.send_static_file('photos/thumbnails/' + filename)


if __name__ == "__main__":
    app.run()
