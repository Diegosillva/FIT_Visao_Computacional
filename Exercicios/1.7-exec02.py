"""
2.O Departamento Estadual de Meteorologia lhe contratou para desenvolver um código que leia um conjunto indeterminado de temperaturas,
 e informe ao final a menor temperatura, a maior temperatura e a média das temperaturas.
 Pare o programa se a temperatura lida for 100.
"""

print("*" * 4, "Departamento Estadual de Meteorologia", "*" * 4)
temperaturas = []

while True:
    temp = float(input("Digite uma temperatura (ou digite 100 pra parar): "))
    if temp == 100:
        break
    temperaturas.append(temp)

if temperaturas:
    menor_temp = min(temperaturas)
    maior_temp = max(temperaturas)
    media_temp = sum(temperaturas) / len(temperaturas)

    print(f"A menor temperatura foi de {menor_temp:.2f}°C")
    print(f"A maior temperatura foi de {maior_temp:.2f}°C")
    print(f"A media das temperaturas foi de {media_temp:.2f}")
else:
    print("Nenhuma temperatura inserida.")
    
