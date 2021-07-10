# import flask
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/chesta')
def chesta():
    return 'OMG!,THIS WEBSITE IS RUNNING'
app.run()