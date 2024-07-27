"""
3.Faça um programa que implemente o filtro “clipe” em uma imagem, ou seja, receba uma imagem em escala de cinza e dois valores: limite inferior e limite superior.
 O filtro funciona da seguinte forma:

a. pixels com valor abaixo do limite inferior recebem o valor do limite inferior;

b. pixels com valor acima do limite superior recebem o valor do limite superior;

Mostre a imagem original e a imagem resultante.
"""

import cv2 as cv
import numpy as np


def aplicar_filtro_clipado(img, limite_inferior, limite_superior):
    imagem_clipada = np.clip(img, limite_inferior, limite_superior)
    return imagem_clipada


img = cv.imread("imagens/fit.png", cv.IMREAD_GRAYSCALE)
limite_inferior = 50
limite_superior = 200
img_cortada = aplicar_filtro_clipado(img, limite_inferior, limite_superior)
cv.imshow("Imagem Original", img)
cv.imshow("Imagem Cortada", img_cortada)
cv.waitKey(0)
cv.destroyAllWindows()
