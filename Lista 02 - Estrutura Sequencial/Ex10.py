'''
Faça um programa que peça a temperatura em Celsius e converta para Fahrenheit. Fórmula: F =
(C * 9/5) + 32.
'''

celsius = float(input("Informe uma temperatura em Celsius: "))
fahrenheit = (celsius * 1.8 + 32)

print("Sua temperatura em Fahrenheit é igual a " + str(fahrenheit))