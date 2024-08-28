# 1.Escreva um programa que detecte cores selecionadas a partir de cliques na imagem da webcam e mostre o resultado em outra janela. Dica: determine os limites de detecção de cores a partir do pixel clicado.


import cv2 as cv
import numpy as np


def click(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        for indx in range(3):
            if imgHSV[y, x][indx] > hsvMax[indx]:
                hsvMax[indx] = imgHSV[y, x][indx]
            if imgHSV[y, x][indx] < hsvMin[indx]:
                hsvMin[indx] = imgHSV[y, x][indx]
        print(hsvMax, hsvMax)


hsvMin = np.array([180, 255, 255])
hsvMax = np.array([0, 0, 0])

webcam = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    img = webcam.read()[1]
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    res = cv.inRange(imgHSV, hsvMin, hsvMax)

    cv.imshow("Web", img)
    cv.setMouseCallback("Web", click)
    cv.imshow("Res", res)
    tecla = cv.waitKey(1)
    if tecla == ord("q"):
        break
