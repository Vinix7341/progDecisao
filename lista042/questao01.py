'''
1. Fazer um algoritmo que peça um número, e ao final, informe se o número digitado está acima de 1000 ou
abaixo de 1000.
'''

num = int(input("Digite um número e lhe direi se ele está acima ou abaixo de 1000:\n"))

res = (f"{num} está abaixo de 1000", f"{num} está acima de 1000")[num > 1000]
print(res)