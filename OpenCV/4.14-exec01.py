# 1.Faça um programa que encontre rostos e olhos na webcam utilizando cascatas de Haar.

import cv2 as cv

web = cv.VideoCapture(0, cv.CAP_DSHOW)
classificador_rosto = cv.CascadeClassifier("face.xml")
classificador_olho = cv.CascadeClassifier("eye.xml")

while True:
    img = web.read()[1]

    img_cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    rosto = classificador_rosto.detectMultiScale(img_cinza)
    olhos = classificador_olho.detectMultiScale(img_cinza)

    for x, y, w, h in rosto:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    for x, y, w, h in olhos:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv.imshow("Web", img)
    tecla = cv.waitKey(1)
    if tecla == ord("q"):
        break
