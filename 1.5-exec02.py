# 2.Faça um programa que peça o raio de um círculo e calcule sua área.
from math import pi

print("0" * 10, "Area do Circulo", "0" * 10)
raio = float(input("Digite raio de um circulo: "))
area = pi * (raio * raio)
print(f"A area do circulo e {area:.2f}")
