'''
7. Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais.
'''

print("Digite dois números e lhe direi qual é o maior e qual é o menor")
v1 = int(input("Digite o primeiro número:\n"))
v2 = int(input("Digite o segundo número:\n"))

if v1 > v2:
    print(f"{v1} é maior do que {v2}")
elif v2 > v1:
    print(f"{v2} é maior do que {v1}")
else:
    print("Ambos são iguais")
