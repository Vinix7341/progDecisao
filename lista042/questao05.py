'''
5. Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
'''

estado = input("Digite a sigla de um estado brasileiro e lhe direi se ele se encontra na região sudeste ou não:\n")

if estado == "RJ" or estado == "SP" or estado == "ES" or estado == "MG":
    print("Esse estado está no sudeste")
else:
    print("Esse estado não faz parte da região sudeste")
