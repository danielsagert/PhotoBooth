import cherrypy
from flask import Flask, send_from_directory
from flask import jsonify

from cam import shoot, get_photos, get_last_photo
from settings import PORT

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
    print('Deliver filenames all photos')
    filenames = get_photos()
    return jsonify(filenames=filenames)


@app.route('/photos/<filename>')
def photo(filename):
    print('Deliver photo: ', filename)
    return send_from_directory('photos', filename)


@app.route('/photos/last')
def new_photo():
    filename = get_last_photo()
    return jsonify(filename=filename)


def run_server():
    # Mount the WSGI callable object (app) on the root directory
    cherrypy.tree.graft(app, '/')

    # Unsubscribe the default server
    cherrypy.server.unsubscribe()

    # Instantiate a new server object
    server = cherrypy._cpserver.Server()

    # Configure the server object
    server.socket_host = "0.0.0.0"
    server.socket_port = PORT
    server.thread_pool = 30

    # Subscribe this server
    server.subscribe()

    # Set the configuration of the web server
    # cherrypy.config.update({
    #     'engine.autoreload_on': True,
    #     'log.screen': True,
    #     'server.socket_port': PORT,
    #     'server.socket_host': '0.0.0.0'
    # })

    # Start the server engine (Option 1 *and* 2)
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == "__main__":
    run_server()
