'''
13) Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente
'''

print("Digite três valores e lhe direi eles em ordem crescente")
a = int(input("Digite o primeiro número:\n"))
b = int(input("Digite o segundo número:\n"))
c = int(input("Digite o terceiro número:\n"))

maior = a

if maior < b:
    maior = b

if maior < c:
    maior = c

menor = a

if menor > b:
    menor = b

if menor > c:
    menor = c

meio = a + b + c - maior - menor

print(f"Os números em ordem crescente são: {menor}, {meio}, {maior}")
