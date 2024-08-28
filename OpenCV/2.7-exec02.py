# 2.Escreva um programa que mostre a imagem da webcam em tempo real equalizada.

import cv2 as cv

webcam = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    img = webcam.read()[1]

    b, g, r = cv.split(img)
    be = cv.equalizeHist(b)
    ge = cv.equalizeHist(g)
    re = cv.equalizeHist(r)
    res = cv.merge((be, ge, re))

    cv.imshow("original", img)
    cv.imshow("Resultado", res)
    tecla = cv.waitKey(1)
    if tecla == ord("q"):
        break
