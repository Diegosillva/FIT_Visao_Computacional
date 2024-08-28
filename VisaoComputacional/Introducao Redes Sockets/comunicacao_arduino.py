from time import sleep
import serial

try:
    conexao = serial.Serial("COM3", baudrate=9600)
    print("Aguarde....")
    sleep(2)
    while True:
        msg = input("Digite uma msg on ou Off\n")
        if msg == "on":
            conexao.write(msg.encode("ascii"))
            sleep(0.2)
        else:
            conexao.write(msg.encode("ascii"))
            sleep(0.2)
            data = conexao.read_all()
            msg = data.decode("ascii")


except Exception as e:
    print("Conexao nao encontrada", e)

