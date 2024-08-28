"""4.Faça um programa para aguçar a imagem da webcam em 4 níveis: sem aguçamento com a tecla “q”, 1 aguçamento com a tecla “w”, 2 aguçamentos com a tecla “e” e 3 aguçamentos com a tecla “r”. Tecla “s” para sair."""

import cv2 as cv

webcam = cv.VideoCapture(0, cv.CAP_DSHOW)

multiplicador = 0
while True:
    img = webcam.read()[1]

    imgEmbacada = cv.blur(img, (5, 5))
    imgDiff = cv.subtract(img, imgEmbacada)
    imgAgucada = cv.add(img, imgDiff * multiplicador)

    cv.imshow("Imagem", img)
    tecla = cv.waitKey(0)
    if tecla == ord("q"):
        multiplicador = 0
    if tecla == ord("w"):
        multiplicador = 1
    if tecla == ord("e"):
        multiplicador = 2
    if tecla == ord("r"):
        multiplicador = 3
    if tecla == ord("s"):
        break
