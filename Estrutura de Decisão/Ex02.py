'''
Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''

valor = float(input("Digite um número: "))

if valor < 0:
    print("Valor negativo!")
elif valor == 0:
    print("Valor neutro!")
else:
    print("Valor positivo!")