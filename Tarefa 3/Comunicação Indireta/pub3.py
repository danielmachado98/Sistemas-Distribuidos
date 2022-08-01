import time
import zmq

context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://127.0.0.1:4000")
print("Publisher 3 Ligado!")

while True:
    publisher.send_multipart(["Jesse".encode(), str(9.4).encode(), str(8.1).encode(), str(7.5).encode()])
    publisher.send_multipart(["Humberto".encode(), str(5.2).encode(), str(6.5).encode(), str(4.9).encode()])
    publisher.send_multipart(["Alex".encode(), str(3.3).encode(), str(1.1).encode(), str(2.2).encode()])
    time.sleep(1)

publisher.close()
context.term()