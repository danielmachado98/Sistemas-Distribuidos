import time
import zmq

context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://127.0.0.1:4000")
print("Publisher 2 Ligado!")

while True:
    publisher.send_multipart(["Matheus".encode(), "Masculino".encode(), str(18).encode()])
    publisher.send_multipart(["Valeria".encode(), "Feminino".encode(), str(22).encode()])
    publisher.send_multipart(["Cintia".encode(), "Feminino".encode(), str(16).encode()])
    time.sleep(1)

publisher.close()
context.term()