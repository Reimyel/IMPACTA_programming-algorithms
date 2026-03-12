'''
Faça um programa que calcule o salário com descontos: IR (11%), INSS (8%) e Sindicato (5%).
Mostrar salário bruto e líquido.
'''

valorHora = float(input("Informe o valor que você ganha por hora: "))
horaMes = float(input("Informe quantas horas você trabalha por mês: "))
salarioBruto = valorHora * horaMes

descontoIR = (11 / 100) * salarioBruto
descontoINSS = (8 / 100) * salarioBruto
descontoSindicato = (5 / 100) * salarioBruto
salarioLiquido = salarioBruto - descontoIR - descontoINSS - descontoSindicato

print("Seu salário bruto por mês é " + str(salarioBruto))
print("Seu salário líquido por mês é " + str(salarioLiquido))