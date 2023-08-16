'''
6. Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo
deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior
que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela:
“Dados inseridos estão incorretos”.
'''

print("Me informe o seu ano de nascimento e o ano atual que direi a sua idade:")
nas = int(input("Digite o seu ano de nascimento:\n"))
ano = int(input("Digite o ano atual:\n"))

if nas < ano:
    print(f"Você tem {ano - nas}")
else:
    print("Dados inseridos estão incorretos")
