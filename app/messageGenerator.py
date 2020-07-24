import os
import sys
import zmq
import time

class MessageClient:
    def __init__(self, addr = 'tcp://127.0.0.1:6000'):
        # connect to message server
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(addr)
    def send(self,msg):
        self.socket.send_string(msg)
        dummy_message = self.socket.recv()

# generate message
w = MessageClient(addr = 'tcp://127.0.0.1:6000')
i = 0
while True:
    w.send(str("hello")+str(i))
    i = i+1
    time.sleep(1)

    # must receive reply before the next send 
   
