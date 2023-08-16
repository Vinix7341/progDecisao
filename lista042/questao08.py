'''
8. Fazer um algoritmo que pergunte 3 números, e ao final, guarde na variável maior o maior destes 3 números
inseridos. O valor da variável maior deverá ser exibido ao final.
'''

print("Digite três números e lhe direi o maior")
v1 = int(input("Digite o primeiro número:\n"))
v2 = int(input("Digite o segundo número:\n"))
v3 = int(input("Digite o terceiro número:\n"))

maior = v1

if maior < v2:
    maior = v2

if maior < v3:
    maior = v3

print(f"O maior número é o {maior}")