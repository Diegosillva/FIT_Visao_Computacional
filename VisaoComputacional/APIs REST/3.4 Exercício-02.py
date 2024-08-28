import base64
from flask import Flask
import cv2 as cv

# 2.Faça um programa que solicite a imagem da webcam do programa anterior e mostre em uma janela. Experimente solicitar a imagem do computador de um colega.

app = Flask("minha Api")
webcam = cv.VideoCapture(0, cv.CAP_DSHOW)


@app.route("/img", methods=["POST", "GET"])
def captura_da_imagem():
    try:
        cap, frame = webcam.read()
        cap, frame = webcam.read()
        retval, buffer = cv.imencode(".png", frame)
        buffer64 = base64.b64encode(buffer)
        return {"img": buffer64.decode("ascii")}, 200
    except KeyError as e:
        return {"erro": f"Campo {e} nao econtrado"}, 400
    except Exception as e:
        return {"erro": f"{e}"}, 400

app.run()

