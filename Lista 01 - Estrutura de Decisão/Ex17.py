'''
Faça um programa que peça um número correspondente a um
determinado ano e em seguida informe se este ano é ou não bissexto.
'''

ano = int(input("Informe um ano no formato a seguir: 2004\n:"))

if ano % 4 == 0: #'%' significa MODULO, e é o que sobra da divisão. % == 0 significa que não sobrou nada (pro beta)
    if ano % 400 == 0:
        print("É um ano bissexto!")
    elif ano % 100 == 0:
        print("Não é um ano bissexto!")
    else:
        print("É um ano bissexto!")
else:
    print("Não é um ano bissexto!")