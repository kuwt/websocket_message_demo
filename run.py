from app import socketapp
from app import socketio

if __name__=='__main__':
    #app.run(debug=True, host='0.0.0.0')
    socketio.run(socketapp,host='0.0.0.0')