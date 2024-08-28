"""
1.Faça um programa que verifique se a nota de um aluno está no intervalo entre 0 e 10.
Mostre uma mensagem caso o valor esteja fora deste intervalo e leia a nota novamente até que o usuário informe um valor válido.

"""

while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if nota <= 10:
        print("Sua nota esta valida. Parabéns!!!")
        break
    else:
        print("Sua nota esta invalida.")
