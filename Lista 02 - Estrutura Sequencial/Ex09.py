'''
Faça um programa que peça a temperatura em Fahrenheit e converta para Celsius. Fórmula: C = 5
* ((F - 32) / 9).
'''

fahrenheit = float(input("Informe uma temperatura em Fahrenheit: "))
celsius = ((fahrenheit - 32) / 1.8)

print("Sua temperatura em Celsius é igual a " + str(celsius))