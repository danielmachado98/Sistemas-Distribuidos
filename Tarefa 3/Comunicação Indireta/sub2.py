import zmq

context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://127.0.0.1:4000")

print("Digite o nome para se inscrever: ")
name = input()
subscriber.setsockopt(zmq.SUBSCRIBE, name.encode())

[n, s, id] = subscriber.recv_multipart()

nome = n.decode()
sexo = s.decode()
idade = int(id.decode())

if sexo == "Masculino" and idade >= 18 or sexo == "Feminino" and idade >= 21:
    resposta = "Atingiu a Maioridade!"
else:
    resposta = "Nao atingiu a Maioridade!"

print(nome+ " " +resposta)

subscriber.close()
context.term()