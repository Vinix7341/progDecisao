'''
5) Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno
'''

print("Me diga 4 notas escolares sua e lhe direi sua média e se você foi aprovado ou reprovado")
v1 = float(input("Digite a sua primeira nota:\n"))
v2 = float(input("Digite a sua segunda nota:\n"))
v3 = float(input("Digite a sua terceira nota:\n"))
v4 = float(input("Digite a sua quarta nota:\n"))

media = (v1 + v2 + v3 + v4) / 4

if media >= 5:
    print(f"Você foi aprovado, parabéns! A sua média é de {media}")
else:
    print(f"Você reprovado, sinto muito! A sua média é de {media}")
