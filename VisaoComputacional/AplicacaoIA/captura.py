# 1.Faça um modelo de rede neural convolucional que classifique suas emoções na webcam, por exemplo: sorrindo, surpreso e neutro.
#  Experimente acrescentar mais camadas convolucionais para melhorar seus resultados.

import os
import cv2 as cv

webcam = cv.VideoCapture(0, cv.CAP_DSHOW)
i_A = len(os.listdir("imagens/class_A"))
i_B = len(os.listdir("imagens/class_B"))
i_C = len(os.listdir("imagens/class_C"))

while True:
    img = webcam.read()[1]

    cv.imshow("tela 1", img)
    tecla = cv.waitKey(1)
    if tecla == ord("a"):
        cv.imwrite(f"imagens/class_A/sorrindo{i_A}.png", img)
        i_A += 1
    if tecla == ord("b"):
        cv.imwrite(f"imagens/class_B/neutro{i_B}.png", img)
        i_B += 1

    if tecla == ord("c"):
        cv.imwrite(f"imagens/class_C/surpresa{i_C}.png", img)
        i_C += 1
    if tecla == ord('q'):
        break    
