import flask
from PIL import Image

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


@app.route('/photos/resize/<filename>')
def resized_photo(filename):
    basewidth = 300
    img = Image.open('photos/' + filename)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    return flask.send_file(img, as_attachment=True, attachment_filename='resized_' + filename)


if __name__ == "__main__":
    app.run()
