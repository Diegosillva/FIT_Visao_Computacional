from flask import Flask, request
import cv2 as cv
import base64

app = Flask("Minha API Soma")
img = cv.imread("fit.jpg")


@app.route("/img", methods=["GET", "POST"])
def imagem_codificada():
    try:
        retval, buffer = cv.imencode(".jpg", img)
        buffer64 = base64.b64encode(buffer)
        string64 = buffer64.decode("ascii")
        return {"Resultado": string64}, 200

    except Exception as e:
        return {"erro": f"{e}"}, 400


app.run()
