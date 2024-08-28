"""1.Escreva um programa que leia dois valores: “x” e “y”.
Utilize estes valores como coordenadas de um pixel em uma imagem qualquer e
mostre os valores dos canais BGR deste pixel. Caso as coordenadas estejam fora da imagem,
imprima a mensagem “Coordenadas inválidas”."""

import cv2 as cv

x = int(input("Digite a coordenada x: "))
y = int(input("Digite a coordenada y: "))

img = cv.imread("imagens/fit.jpg")
linhas, colunas, canais = img.shape

if x < linhas and y < colunas:
    pixel = img[x, y]
    print(f"Coordenada valida {pixel}")
else:
    print("Coordenada invalidas")
