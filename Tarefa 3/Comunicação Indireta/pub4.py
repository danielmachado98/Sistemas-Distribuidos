import time
import zmq

context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://127.0.0.1:4000")
print("Publisher 4 Ligado!")

while True:
    publisher.send_multipart(["Marcos".encode(), str(1.84).encode(), "Masculino".encode()])
    publisher.send_multipart(["Amanda".encode(), str(1.65).encode(), "Feminino".encode()])
    publisher.send_multipart(["Vitoria".encode(), str(1.72).encode(), "Feminino".encode()])
    time.sleep(1)

publisher.close()
context.term()