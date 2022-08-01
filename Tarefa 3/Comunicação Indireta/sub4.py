import zmq

context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://127.0.0.1:4000")

print("Digite o nome para se inscrever: ")
name = input()
subscriber.setsockopt(zmq.SUBSCRIBE, name.encode())

[n, alt, s] = subscriber.recv_multipart()

nome = n.decode()
altura = float(alt.decode())
sexo = s.decode()

if sexo == "Masculino":
    peso = (72.7*altura)-58
elif sexo == "Feminino":
    peso = (62.1*altura)-44.7

print("Peso ideal de " +nome+ ": %.2f" % peso)

subscriber.close()
context.term()