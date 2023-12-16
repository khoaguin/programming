#
#   Request-reply service in Python
#   Connects REP socket to tcp://localhost:5560
#   Expects "Hello" from client, replies with "World"
#
import zmq

print("rrworker")

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:5560")

total_req = 0
while True:
    message = socket.recv()
    total_req += 1
    print(f"Received request # {total_req}: {message}")
    socket.send(b"World")
