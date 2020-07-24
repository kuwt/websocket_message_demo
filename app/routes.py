from flask import render_template
from flask_socketio import send, emit

from app import socketapp
from app import socketio
import os
import sys
import time
import threading
import zmq

@socketapp.route('/')
@socketapp.route('/index')
def index():
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
#MessageServer
######################################
class MessageServer:
    def __init__(self, addr = 'tcp://127.0.0.1:6000', handler = None):
        # connect to message server
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind(addr)
        self.msghandler = handler

    def msgHandlerThread(self):
        while True:
            msg = self.socket.recv()
            decode_msg = msg.decode("utf-8")
            if self.msghandler != None:
                self.msghandler(decode_msg)
            self.socket.send_string("noted")

    def start(self):
        thread = threading.Thread(target=self.msgHandlerThread)
        thread.start()


def messageGenerator():
    print("current directory = {}".format(os.getcwd()))
    os.system('python3 ./app/messageGenerator.py')

def msgHandler(msg):
    socketio.send(msg)
######################################
# main
w = MessageServer(addr = 'tcp://127.0.0.1:6000',handler = msgHandler)
w.start()

thread2 = threading.Thread(target=messageGenerator)
thread2.start()





