from flask import Flask
from flask_socketio import SocketIO
import os

socketapp = Flask(__name__)
socketio = SocketIO(socketapp)

from app import routes
