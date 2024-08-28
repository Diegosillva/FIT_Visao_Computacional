import cv2 as cv
from flask import Flask

# 1.Faça um programa em Flask que forneça a imagem da webcam na rota /img.

app = Flask("minha imagem")


@app.route("/img", methods=["GET"])
def minha_imagem():
    webcam = cv.VideoCapture(0, cv.CAP_DSHOW)

    while True:
        _, img = webcam.read()
        cv.imshow("minha imagem", img)
        if cv.waitKey(1) == ord("q"):
            break


app.run()
