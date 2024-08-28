# 1.Faça um programa que leia uma coordenada na imagem (x e y) e a área de um círculo. Desenhe um círculo na imagem com base nestas duas informações.

from numpy import sqrt, pi
import cv2 as cv

# (580, 870, 3)
x = int(input("Digite uma coordenada entre (580 e 870), x: "))
y = int(input("Digite uma coordenada entre (580 e 870), y: "))
area = float(input("Digite uma area: "))
img = cv.imread("imagens/moon.jpg")
fonte = cv.FONT_ITALIC
origem = (300, 300)
cor = (0, 255, 0)
raio = int(sqrt(area / pi))
cv.putText(img, "Lua", origem, fonte, 5, cor, 5)
circulo = cv.circle(img.copy(), (x, y), raio, (0, 0, 255), 3)

cv.imshow("Lua", circulo)
cv.waitKey(0)
cv.destroyAllWindows()
