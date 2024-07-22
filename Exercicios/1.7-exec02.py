"""
2.O Departamento Estadual de Meteorologia lhe contratou para desenvolver um código que leia um conjunto indeterminado de temperaturas
 e informe ao final a menor temperatura, a maior temperatura e a média das temperaturas. Pare o programa se a temperatura lida for 100.
"""

print("Departamento Estadual de Meterologia")
temperaturas = []
while True:
    temp = float(input("Digite a temperatura (ou 100 para parar ): "))
    if temp == 100:
        break
    temperaturas.append(temp)
if temperaturas:
    menor_temp = min(temperaturas)
    maior_temp = max(temperaturas)
    media_temp = sum(temperaturas) / len(temperaturas)
    print(f"A menor temperatura foi de: {menor_temp}°C")
    print(f"A maior temperatura foi de: {maior_temp}°C")
    print(f"A media das temperatura foi de: {media_temp:.2f}")
else:
    print("Nenhuma temperatura foi inserida")
