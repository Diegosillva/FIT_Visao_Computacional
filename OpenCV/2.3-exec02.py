"""2.Escreva um programa que leia valores para dois pixels da imagem e “pinte” a região entre esses dois pixels com a cor verde."""

import cv2 as cv

# linha1 = input("Digite uma coordenada: ")
# coluna1 = input("Digite uma coordenada: ")
# linha2 = input("Digite uma coordenada: ")
# coluna2 = input("Digite uma coordenada: ")

img = cv.imread("imagens/fit.png")
linha, coluna, canais = img.shape
img[200:200, 150:150] = [255, 0, 0]
cv.imshow("FIT Logo", img)
cv.waitKey(0)
