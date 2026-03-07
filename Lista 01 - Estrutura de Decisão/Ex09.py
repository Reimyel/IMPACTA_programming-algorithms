'''
Faça um programa que leia três números e mostre-os em ordem decrescente.
'''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if ((num1 > num2) and (num1 > num3)):
    print(str(num1))
    if ((num2 > num3)):
        print(str(num2))
        print(str(num3))
    else:
        print(str(num3))
        print(str(num2))
#
elif ((num2 > num1) and (num2 > num3)):
    print(str(num2))
    if ((num1 > num3)):
        print(str(num1))
        print(str(num3))
    else:
        print(str(num3))
        print(str(num1))
#
elif ((num3 > num1) and (num3 > num2)):
    print(str(num3))
    if ((num1 > num2)):
        print(str(num1))
        print(str(num2))
    else:
        print(str(num2))
        print(str(num1))
#
else:
    print("Esses números são os mesmos!")