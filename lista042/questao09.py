'''
9. Fazer um algoritmo que pergunte a idade de uma pessoa, e ao final, informe na tela se a pessoa é menor de
idade, se é maior de idade, ou se é maior de 65 anos.
'''

idade = int(input("Digite a sua idade:\n"))

if idade < 18:
    print("Você é menor de idade")
elif idade <= 65:
    print("Você é maior de idade")
else:
    print("Você é maior de 65 anos")
