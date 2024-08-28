# 2.Faça um programa que desenhe em uma imagem como um pincel vermelho do paint.


import cv2 as cv

botao_pressionado = False


def click(event, x, y, flags, params):
    global botao_pressionado
    if event == cv.EVENT_LBUTTONDOWN:
        botao_pressionado = True
    if event == cv.EVENT_LBUTTONUP:
        botao_pressionado = False
    if event == cv.EVENT_MOUSEMOVE and botao_pressionado:
        cv.circle(img, (x, y), 5, (0, 0, 255), -1)


img = cv.imread("imagens/robot.jpg")
while True:
    cv.imshow("imagem", img)
    cv.setMouseCallback("imagem", click)
    tecla = cv.waitKey(1)
    if tecla == ord("q"):
        break
