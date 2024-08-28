# 1.Escreva um programa que abra a imagem “celularRuido.jpg” e elimine o ruído dos pixels vermelhos.
import cv2 as cv

img = cv.imread("imagens/celularRuido.jpg")
ruido = cv.medianBlur(img, 3)
ruido2 = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow("Ruido 2", ruido2)
cv.imshow("Remoção do Ruido", ruido)
cv.waitKey(0)
