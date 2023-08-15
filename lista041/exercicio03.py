'''
3) Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par ou
é ímpar.
'''

num = float(input("Digite um número e te direi se é par ou ímpar:\n"))

rest = num % 2

if rest == 1:
    print(f"O número {rest} é ímpar")
else:
    print(f"O número {rest} é par")
