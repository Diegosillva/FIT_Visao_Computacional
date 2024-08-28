# 1.Faça um programa que leia um número de 1 a 4 e aplique essa quantidade de erosões em uma imagem.

import cv2 as cv
import numpy as np

img = cv.imread("imagens/opencv.png")
cv.imshow("Original", img)

quantidade = int(input("Digite um numero de 1 a 4"))
kernel = np.ones((5, 5))

for i in range(quantidade):
    img = cv.erode(img, kernel)

cv.imshow("resultado", img)
cv.waitKey(0)
cv.destroyAllWindows()
