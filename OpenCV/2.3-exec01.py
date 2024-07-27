"""
1.Escreva um programa que leia dois valores: “x” e “y”.
Utilize estes valores como coordenadas de um pixel em uma imagem qualquer e mostre os valores dos canais BGR deste pixel.
Caso as coordenadas estejam fora da imagem, imprima a mensagem “Coordenadas inválidas”.
"""

import cv2 as cv

x = int(input("Digite uma coordenada x: "))
y = int(input("Digite uma coordenada y: "))

img = cv.imread("imagens/fit.png")
coordenadas = x, y
pixel = img.shape
if coordenadas < pixel:
    print("Coordenada Valida")
else:
    print("Coordenada Invalida")
print(pixel)
