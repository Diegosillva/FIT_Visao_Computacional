"""2.Escreva um programa que leia valores para dois pixels da imagem e “pinte”
a região entre esses dois pixels com a cor verde."""

import cv2 as cv

linha1 = int(input("Digite a coordenada x1: "))
coluna1 = int(input("Digite a coordenada y1: "))
linha2 = int(input("Digite a cooordenada y1: "))
linha2 = int(input("Digite a coordenada x2: "))
coluna2 = int(input("Digite a coordenada y2: "))

img = cv.imread("imagens/fit.jpg")

img[linha1:linha2, coluna1:coluna2] = [0, 255, 0]
cv.imshow("fit log", img)
cv.waitKey(0)
