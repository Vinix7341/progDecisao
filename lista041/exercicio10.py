'''
10) Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo
número informado é ou não um divisor do primeiro número informado
'''

print("Digite dois números inteiros e lhe direi se o segundo é divisor do primeiro")
num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

rest = num1 % num2

if rest == 0:
    print(f"O número {num2} é divisor do número {num1}")
else:
    print(f"O número {num2} não é divisor do número {num1}")