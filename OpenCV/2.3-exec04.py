"""
4.Escreva um programa que tente achar um pixel vermelho na imagem e mostre suas coordenadas.
 Caso não haja pixel vermelho, imprima a mensagem “Sem vermelho”. Utilize os valores BGR [0, 0, 255]
"""

import cv2 as cv

img = cv.imread("imagens/opencv.png")
linhas, colunas, canais = img.shape
achouVermelho = False

for indexLinha in range(linhas):
    for indexColuna in range(colunas):
        pixel = img[indexLinha, indexColuna]
        b, g, r = pixel
        if b == 0 and g == 0 and r == 255:
            achouVermelho = True
            print(f"Coordenada do Vermelho: {indexLinha}, {indexColuna}")
if not achouVermelho:
    print("Sem Vermelho")
