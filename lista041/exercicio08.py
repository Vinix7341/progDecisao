'''
8) Desenvolver um programa que pergunte um número inteiro qualquer e verifique se ele está na faixa de 1 a 10
'''

num = int(input("Digite um número inteiro:\n"))

if num >= 1 and num <= 10:
    print(f"O número {num} está na faixa de 1 a 10")
else:
    print(f"O número {num} não está na faixa de 1 a 10")
