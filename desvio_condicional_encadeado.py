'''
Crie um programa que pergunte um número ao usuário. Em seguida o programa deve informar se o número inserido está abaixo de 100, entre 100 e 200 ou acima de 200.
'''

num = int(input("Digite um número:\n"))

if (num < 100):
    print(f"{num} está abaixo de 100")
else:
    if (num <= 200):
        print(f"{num} está entre 100 e 200")
    else:
        print(f"{num} está acima de 200")