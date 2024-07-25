"""
1.Faça um programa que gerencie um estoque de produtos de um supermercado em uma lista.

Cada produto deve ser um dicionário que possui os seguintes campos:
nome;
preço;
quantidade em estoque.
Seu programa deve ter um pequeno menu que possua as funções abaixo:

"""

import os


# menu
def menu():
    print("#" * 20)
    print("#" * 1, "Supermercado FIT", "#" * 1)
    print("#" * 20)

    print(
        "1 - Casdastrar novo Produto.\n2 - Custo Financeiro.\n3 - Quantidade de Produtos.\n0 - Sair.\n"
    )
    

estoque = []


# a) Cadastro de um novo produto no estoque.
def cadastrar_produtos():
    global estoque
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o valor do Produto: "))
    quantidade_produto = int(input("Digite a quantidade do Produto: "))
    produto = {"nome": nome, "preco": preco, "quantidade_produto": quantidade_produto}
    estoque.append(produto)
    return estoque


# c) Visualizar a quantidade de todos os produtos, mostrando “nome” e “quantidade” de todos os produtos do estoque.
def quantidade_produto():
    global estoque
    for produto in estoque:
        nome = produto["nome"]
        qtd_produto = produto["quantidade_produto"]
        print("#" * 4, "Supermercado FIT Estoque", "#" * 4)
        print(f"Nome do Produto: {nome}")
        print(f"Quantidade Estoque: {qtd_produto} \n")


# b) Visualizar o total financeiro de um produto, pesquisando por nome ou pelo índice na lista.
def valor_produto(nome_produto):
    global estoque
    for produto in estoque:
        if produto["nome"] == nome_produto:
            return produto["preco"]
    return print("Produto não encontrado ou não cadastrado")


while True:
    menu()
    opcao = input("Digite uma opcão: ")
    os.system("clear")
    if opcao == "1":
        produto = cadastrar_produtos()
        print("Produto cadastrado com sucesso.\n")
    elif opcao == "2":
        produto_pequisado = input("Digite o nome do Produto: ")
        preco = valor_produto(produto_pequisado)
        print(
            f"O produto encontrado foi {produto_pequisado} e seu valor e de R$ {preco:.2f}"
        )
    elif opcao == "3":
        quantidade_produto()
    if opcao == "0":
        print("Muito obrigado, saindo do programa.")
        break
