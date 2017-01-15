from flask import Flask, render_template
from flask import jsonify

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

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
