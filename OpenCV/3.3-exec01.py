"""1.Você está trabalhando em um projeto de um carro sem motorista. Uma tarefa é detectar as faixas das ruas para guiar o carro. Utilize a função Canny para segmentar as bordas da imagem “estrada.jpg”. Experimente diferentes limiares."""

import cv2 as cv

img = cv.imread("imagens/estrada.jpg", cv.IMREAD_GRAYSCALE)
bordas = cv.Canny(img, 100, 200)
cv.imshow("Imagem", bordas)
cv.waitKey(0)
