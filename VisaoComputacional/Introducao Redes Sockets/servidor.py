import socket


def menu():
    print("Ola me chamo Diego em que posso ajuda.")


def servidor():
    try:
        ip = "10.113.163.201"  # 10.113.163.201
        port = 8000
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind((ip, port))
        servidor.listen()
        print("Aguardando cliente.....")
        cliente, endereco = servidor.accept()
        msg = "Em que posso ajuda.\n"
        msg_bytes = msg.encode("ascii")
        cliente.send(msg_bytes)
        msg_bytes = cliente.recv(1024)
        print(msg_bytes.decode("ascii"))
        cliente.close()
    except Exception as e:
        print("Erro na conexao: ", e)


while True:
    try:
        servidor()
    except Exception as msg:
        print("Servidor nao Encontrado.", msg)
