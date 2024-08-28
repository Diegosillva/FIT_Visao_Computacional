import cv2 as cv

img = cv.imread("imagens/fit.jpg")
azul, verde, vermelho = cv.split(img)
img = cv.merge((azul, verde, vermelho))
img[img > 100] = 255

cv.imshow("Logo do FIT", img)
cv.waitKey(0)
