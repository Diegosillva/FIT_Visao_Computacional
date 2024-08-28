"""3.Faça a brincadeira da estátua com a webcam. Ao digitar a letra “e”, salve um frame em uma variável e o subtraia das próximas imagens em tempo real, mostrando a imagem resultante da subtração binarizada em uma janela. Para sair, o programa detecta a letra “s”.

Dica: atribua “None” para iniciar a variável que materá o frame da estátua e o verifique com “if frameEstatua is None:”."""

import cv2 as cv

webcam = cv.VideoCapture(0, cv.CAP_DSHOW)
frame_estatua = None
while True:
    frame_atual = webcam.read()[1]

    if frame_estatua is None:
        cv.imshow("imagem", frame_atual)
    else:
        img_subtracao = cv.subtract(frame_estatua, frame_atual)
        cv.imshow("imagem", img_subtracao)

    tecla = cv.waitKey(1)
    if ord("s") == tecla:
        break
    if ord("e") == tecla:
        frame_estatua = frame_atual
    if ord("s") == tecla:
        frame_estatua = None
