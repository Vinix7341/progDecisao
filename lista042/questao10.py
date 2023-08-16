'''
10. Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela
como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições
devem seguir as regras da tabela abaixo:
'''

print("Me diga as suas duas notas da prova e lhe direi sua média e se você foi aprovado")
v1 = float(input("Digite a nota da primeira prova:\n"))
v2 = float(input("Digite a nota da segunda prova:\n"))

media = (v1 + v2) / 2

if media < 3:
    print("Você foi reprovado")
elif media < 7:
    print("Você irá fazer prova final")
else:
    print("Você foi aprovado")