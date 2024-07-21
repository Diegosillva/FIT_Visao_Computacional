# 1.Faça um programa que peça as 4 notas de um aluno e mostre a média final.

print("*" * 10, "Nota do aluno", "*" * 10)
primeira_nota = float(input("Digite sua nota (N1):  "))
segunda_nota = float(input("Digite sua nota (N2):  "))
terceira_nota = float(input("Digite sua nota (N3):  "))
quarta_nota = float(input("Digite sua nota (N4):  "))

media = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4
if media <= 5:
    print(f"Sua media foi de {media}, Você esta Reprovado")
else:
    print(f"Sua media foi de {media}, Parabéns você foi Aprovado")

# nota = (f'Sua media final foi de {media}')
