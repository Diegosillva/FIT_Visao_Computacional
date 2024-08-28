"""
3.Observe na variável a seguir que cada elemento é uma lista. Portanto, podemos chamar estes dados de “matrix”.
Faça um programa que para cada número na lista, mostre seu valor em somado de 1.

números = [

[3, 5, 1],

[-1, 1, 0],

[2, -3, 1]

]
"""

numeros = [[3, 5, 1], [-1, 1, 0], [2, -3, 1]]
for linha in numeros:
    for numero in linha:
        print(numero + 1)
