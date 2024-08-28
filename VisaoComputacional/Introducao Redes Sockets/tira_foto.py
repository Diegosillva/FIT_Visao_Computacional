from time import sleep

import cv2 as cv
import serial


class Arduino:
    def abrir_camera():
        webcam = cv.VideoCapture(0, cv.CAP_DSHOW)
        frame, img = webcam.read()
        webcam.release()
        if not frame:
            return None
        return img

    def identificar_cor(img):
        medias = cv.mean(img)
        b, g, r, _ = medias
        if r > g and r > b:
            return "vermelho"
        elif g > r and g > b:
            return "verde"
        elif b > r and b > g:
            return "azul"
        else:
            return "indefinido"

    try:
        conexao = serial.Serial("COM3")
        print("Aguarde....")
        sleep(2)
        while True:
            data = conexao.read_all()
            msg = data.decode("ascii").split()
            if "foto" in msg:
                img = abrir_camera()
                if img is not None:
                    cor = identificar_cor(img)
                    conexao.write(cor.encode("ascii"))
                else:
                    print("Erro ao capturar foto".encode("ascii"))
            sleep(1)

    except Exception as e:
        print("erro na conexao...", e)


arduino = Arduino()
