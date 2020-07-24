from flask import render_template
from flask_socketio import send, emit

from app import socketapp
from app import socketio
import time
import threading

@socketapp.route('/')
@socketapp.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user="test1")

@socketapp.route('/hello')
def hello():
    return 'Hello, hello_world!'


######################################
# socketio handling
######################################
@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    send(message + 'by server')
    return 0

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))
    return 0

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    return 0

@socketio.on('connect')
def test_connect():
    print('Client connect')

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

######################################
# background_calculation
######################################
def background_calculation():
    i = 0
    while True:
        socketio.send("hallo " + str(i))
        i = i+1
        time.sleep(1)

thread = threading.Thread(target=background_calculation)
thread.start()
