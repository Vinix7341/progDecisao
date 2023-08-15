'''
4) Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja
divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por
4 e 5”.
'''

num = int(input("Digite um número e lhe direi se ele é divisível por 4 e 5:\n"))

quatro = num % 4
cinco = num % 5

if quatro == 0 and cinco == 0:
    print(f"O valor {num} é divisível por 4 e 5")
else:
    print("Valor não é divisível por 4 e 5")