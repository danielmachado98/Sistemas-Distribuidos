import time
import zmq

context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://127.0.0.1:4000")
print("Publisher 1 Ligado!")

while True:
    publisher.send_multipart(["Sergio".encode(), "Operador".encode(), str(3000).encode()])
    publisher.send_multipart(["Daniel".encode(), "Programador".encode(), str(1500).encode()])
    publisher.send_multipart(["Ana".encode(), "Programador".encode(), str(2000).encode()])
    time.sleep(1)

publisher.close()
context.term()