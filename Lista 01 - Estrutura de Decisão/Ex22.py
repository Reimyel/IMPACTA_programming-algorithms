'''
Faça um programa que peça um número inteiro e determine se ele é
par ou ímpar. Dica: utilize o operador módulo (resto da divisão).
'''

num = (int(input("Informe um número inteiro: ")))
numMod = num % 2

if numMod == 0:
    print("Seu número é par!")
else:
    print("Seu número é impar!")