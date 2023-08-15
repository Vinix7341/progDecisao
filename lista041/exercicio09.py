'''
9) Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou
nulo.
'''

num = float(input("Digite um número:\n"))

if num == 0:
    print("Seu número é nulo")
elif num > 0:
    print("Seu número é positivo")
else:
    print("Seu número é negativo")