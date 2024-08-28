"""1.Escreva um programa que tenha um laço de repetição, que reduza uma imagem de 1 a 100 vezes e transforme a imagem reduzida de volta ao tamanho original com interpolação por proximidade (Nearest). Mostre as imagens resultantes na mesma janela."""

import cv2 as cv

img = cv.imread("imagens/chuva.jpg")
cv.imshow("Original", img)

for i in range(100, 1, -1):
    reduzida = cv.resize(img, None, fx=1 / i, fy=1 / i)
    original = cv.resize(reduzida, None, fx=i, fy=i, interpolation=cv.INTER_NEAREST)
    cv.imshow("Original", img)
    cv.imshow("Tamanho Original", original)
    cv.imshow("Reduzida", reduzida)
    cv.waitKey(200)
