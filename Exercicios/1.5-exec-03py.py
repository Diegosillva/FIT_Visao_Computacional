# Um posto está vendendo combustíveis com a seguinte tabela de descontos abaixo.
# 1 - Escreva um programa que leia o número de litros vendidos,
# 2 - o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
#  3 e ao final imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro
#  da gasolina é R$ 6,50 o preço do litro do álcool é R$ 5,60:

# Álcool:
# a. até 20 litros, desconto de 3% por litro

# b. acima de 20 litros, desconto de 5% por litro

# Gasolina:
# a. até 20 litros, desconto de 4% por litro

# b. acima de 20 litros, desconto de 6% por litro
def mostrar_menu():
    print("Meu combustivel")
    print("A - Alcool")
    print("G - Gasolina")


def calcular_preco_desconto(litro, preco_litro, desconto):
    sem_desconto = litro * preco_litro
    com_desconto = sem_desconto * desconto
    total = sem_desconto - com_desconto

    return total


mostrar_menu()
# calcular_preco_desconto()
opcao = input("Digite uma opção: ").upper()
qtd_combustivel = float(input("Quantos litros de combustivel deseja: "))

if opcao == "A":
    preco_litro = 5.60

    if qtd_combustivel <= 20:
        total_pagar = calcular_preco_desconto(qtd_combustivel, preco_litro, 0.03)
        print(f"O total a pagar com desconto de 3% foi de R$ {total_pagar:.2f}")
    else:
        total_pagar = calcular_preco_desconto(qtd_combustivel, preco_litro, 0.05)
        print(f"O total a pagar com desconto de 5% foi de R$ {total_pagar:.2f}")

elif opcao == "G":
    preco_litro = 6.50
    if qtd_combustivel <= 20:
        total_pagar = calcular_preco_desconto(qtd_combustivel, preco_litro, 0.04)
        print(f"O total a pagar com desconto de 4% foi de R$ {total_pagar:.2f}")
    else:
        total_pagar = calcular_preco_desconto(qtd_combustivel, preco_litro, 0.06)
        print(f"O total a pagar com desconto de 6% foi de R$ {total_pagar:.2f}")
