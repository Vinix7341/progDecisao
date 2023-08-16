'''
4. Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana.
'''

num = int(input("Digite um número de 1 a 7 e lhe direi o dia da semana correspondente ao digitado:\n"))

if num == 1:
    print("O dia da semana é domingo")
elif num == 2:
    print("O dia da semana é segunda-feira")
elif num == 3:
    print("O dia da semana é terça-feira")
elif num == 4:
    print("O dia da semana é quarta-feira")
elif num == 5:
    print("O dia da semana é quinta-feira")
elif num == 6:
    print("O dia da semana é sábado")
elif num == 7:
    print("O dia da semana é domingo")
else:
    print("Número inválido")