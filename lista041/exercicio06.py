'''
6) Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o
maior valor e o menor valor lido
'''

print("Me diga dois números inteiros e lhe drei a diferença entre o maior e o menor")
num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

if num1 >= num2:
    print(f"A diferença do maior número pelo menor é de {num1 - num2}")
else:
    print(f"A diferença do maior número pelo menor é de {num2 - num1}")