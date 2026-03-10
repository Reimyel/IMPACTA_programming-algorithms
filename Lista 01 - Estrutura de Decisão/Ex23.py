'''
Faça um programa que peça um número e informe se o número é
inteiro ou decimal. Dica: utilize uma função de arredondamento.
'''
''''''
num = float(input("Informe um número: "))
numArrd = round(num)

if num == numArrd:
    print("Seu número é inteiro")
else:
    print("Seu número é decimal")