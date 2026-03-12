'''
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no
mês. Calcule e mostre o salário total do mês.
'''

valorHora = float(input("Informe o valor que você ganha por hora: "))
horaMes = float(input("Informe quantas horas você trabalha por mês: "))
salarioTotal = valorHora * horaMes

print("Seu salário total por mês é " + str(salarioTotal))