'''
Faça um programa que leia três números e mostre o maior e o menor deles.
'''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if ((num1 > num2) and (num1 > num3)):
    print("Número Maior: " + str(num1))
elif ((num2 > num1) and (num2 > num3)):
    print("Número Maior: " + str(num2))
elif ((num3 > num1) and (num3 > num2)):
    print("Número Maior: " + str(num3))
else:
    print("Os três números são iguais!")
    exit

if ((num1 < num2) and (num1 < num3)):
    print("Número Menor: " + str(num1))
elif ((num2 < num1) and (num2 < num3)):
    print("Número Menor: " + str(num2))
elif ((num3 < num1) and (num3 < num2)):
    print("Número Menor: " + str(num3))