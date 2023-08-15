'''
12) Desenvolver um programa que pergunte 5 números inteiros e identifique o maior número e o menor número.
'''

print("Diga 5 números inteiros e lhe direi o maior número e o menor número")
v1 = int(input("Digite o primeiro número:\n"))
v2 = int(input("Digite o segundo número:\n"))
v3 = int(input("Digite o terceiro número:\n"))
v4 = int(input("Digite o quarto número:\n"))
v5 = int(input("Digite o quinto número:\n"))

maior = v1

if maior < v2:
    maior = v2

if maior < v3:
    maior = v3

if maior < v4:
    maior = v4

if maior < v5:
    maior = v5

menor = v1

if menor > v2:
    menor = v2

if menor > v3:
    menor = v3

if menor > v4:
    menor = v4

if menor > v5:
    menor = v5

print(f"O maior número é {maior} e o menor número é {menor}")
