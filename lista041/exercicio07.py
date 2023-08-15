'''
7) Desenvolver um programa que pergunte um valor inteiro positivo ou negativo, e exiba como resposta o módulo
deste valor, ou seja, o número lido como sendo positivo.
'''

num = int(input("Digite um número inteiro negativo ou positivo e lhe direi o seu módulo:\n"))

if num >= 0:
    print(f"O módulo do seu número é {num}")
else:
    mod = num * -1
    print(f"O módulo do seu número é {mod}")