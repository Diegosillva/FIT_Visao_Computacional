# 1.Faça um programa que desenhe um quadrado preto em torno de um pixel, clicando com o mouse em uma imagem.
# res3 = cv.rectangle(img.copy(), (100, 100), (150, 120), (0, 0, 255), thickness=3)
import cv2 as cv


def click(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 0, 0), -1)


img = cv.imread("imagens/moon.jpg")

while True:
    cv.imshow("imagem", img)
    cv.setMouseCallback("imagem", click)
    tecla = cv.waitKey(1)
    if tecla == ord("q"):
        break
