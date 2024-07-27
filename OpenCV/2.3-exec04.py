"""
4.Escreva um programa que tente achar um pixel vermelho na imagem e mostre suas coordenadas.
 Caso não haja pixel vermelho, imprima a mensagem “Sem vermelho”. Utilize os valores BGR [0, 0, 255]
"""

import cv2 as cv

img = cv.imread("imagens/flex.png")
pixel_vermelho = [0, 0, 255]
img[100:200, 100:200] = pixel_vermelho
cv.imshow("Flex logo", img)
cv.waitKey(0)
cv.destroyAllWindows()
