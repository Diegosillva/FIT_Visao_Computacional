"""
3.Um posto está vendendo combustíveis com a seguinte tabela de descontos abaixo.
 Escreva um programa que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
e ao final imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 6,50 o preço do litro do álcool é R$ 5,60:

Álcool:
a. até 20 litros, desconto de 3% por litro

# b. acima de 20 litros, desconto de 5% por litro

Gasolina:
a. até 20 litros, desconto de 4% por litro

b. acima de 20 litros, desconto de 6% por litro
"""


def calcular_preco_desconto(preco_por_litro, litros, desconto):
    valor_sem_desconto = litros * preco_por_litro
    desconto_total = valor_sem_desconto * desconto
    total_pagar = valor_sem_desconto - desconto_total
    return total_pagar

def menu_combustivel():
    print("Combustivel Disponivel")
    print("[A] - Alcool")
    print("[G] - Gasolina")


menu_combustivel()
opcao = input("Selecione uma opção: ").upper()
qtd_combustivel = float(input("Quantos litros de Combustivel foram vendidos: "))

if opcao == "A":
    preco_por_litro = 5.60
    if qtd_combustivel <= 20:
        total_pagar = calcular_preco_desconto(preco_por_litro, qtd_combustivel, 0.03)
        print(f"Total a pagar com desconto de 3% foi de R$ {total_pagar:.2f}")

    else:
        total_pagar = calcular_preco_desconto(preco_por_litro, qtd_combustivel, 0.05)
        print(f"Total a pagar com desconte de 5% foi de R$ {total_pagar:.2f}")

if opcao == "G":
    preco_por_litro = 6.50
    if qtd_combustivel <= 20:
        total_pagar = calcular_preco_desconto(preco_por_litro, qtd_combustivel, 0.4)
        print(f"Total a pagar com desconto de 4% foi de R$ {total_pagar:.2f}")
    else:
        total_pagar = calcular_preco_desconto(preco_por_litro, qtd_combustivel, 0.6)
        print(f"Total a pagar com desconto de 6% foi de R$ {total_pagar:.2f}")
