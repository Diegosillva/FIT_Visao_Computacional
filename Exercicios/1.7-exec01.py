"""
1.Faça um programa que verifique se a nota de um aluno está no intervalo entre 0 e 10.
 Mostre uma mensagem caso o valor esteja fora deste intervalo e leia a nota novamente até que o usuário informe um valor válido.
"""

while True:
    nota = float(input("Digite a nota do aluno entre 0 e 10: "))
    if nota <= 0 or nota <= 10:
        print("Nota válida. Parabens.")
        break
    else:
        print("Nota inválida. Por favor, insira uma nota entre 0 e 10")
