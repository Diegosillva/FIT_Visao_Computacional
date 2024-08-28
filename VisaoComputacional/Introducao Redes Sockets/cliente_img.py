import socket

IP = "10.113.163.201"
porta = 8000

try:
    while True:
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conexao.connect((IP, porta))
        msg_bytes = conexao.recv(1024)
        print(msg_bytes.decode("ascii"))
        msg = 'Envie as coordenadas.'
        conexao.send(msg.encode("ascii"))
        conexao.close()
except Exception as msg:
    print("Erro na conexao", msg)
