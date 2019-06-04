import zmq
import random
import sys
import time

port = "5559"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://localhost:{}".format(port))
publisher_id = random.randrange(0,9999)
while True:
    topic = "9"
    #random.randrange(1,10)
    messagedata = "server#{}".format(publisher_id)
    print("{} {}".format(topic, messagedata))
    socket.send_string("{} {}".format(topic, messagedata))
    time.sleep(1)

