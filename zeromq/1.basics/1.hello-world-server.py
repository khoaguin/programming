import time

import zmq

print(f"Current libzmq version is {zmq.zmq_version()}")
print(f"Current pyzmq version is {zmq.__version__}")

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print(f"Received request: {message}")

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send_string("World")
