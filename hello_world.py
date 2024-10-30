# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def world():
  return '<p>Gerardo: LOL</p><p>Brandon: BRB</p><p>Milo: YOLO</p>'

@app.route('/zainab')
def hello():
  return render_template('template.html')