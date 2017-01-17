from flask import Flask, render_template
from flask import jsonify
from camera import Camera
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
   return render_template('photo.html',
                           title='Last photo',
                           text='Not implemented yet')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=settings.PORT)
