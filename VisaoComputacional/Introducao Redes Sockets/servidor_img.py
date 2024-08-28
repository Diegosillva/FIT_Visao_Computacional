import socket
from face import image

ip = "10.113.163.201"  # 10.113.163.201
port = 8000
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((ip, port))
servidor.listen()


def servidor01():
    global servidor
    try:
        print("Aguardando cliente.....")
        cliente, endereco = servidor.accept()
        msg = image()
        msg_bytes = msg.encode("ascii")
        cliente.send(msg_bytes)
        msg_bytes = cliente.recv(1024)
        print(msg_bytes.decode("ascii"))
        cliente.close()
    except Exception as e:
        print("Erro na conexao: ", e)


while True:
    servidor01() 
