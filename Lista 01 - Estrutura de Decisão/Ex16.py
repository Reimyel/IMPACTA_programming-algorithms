'''
Faça um programa que calcule as raízes de uma equação do
segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c
e fazer as consistências, informando ao usuário nas seguintes situações:
• Se o usuário informar o valor de A igual a zero, a equação não é do segundo
grau e o programa não deve pedir os demais valores, sendo encerrado;
• Se o delta calculado for negativo, a equação não possui raízes reais.
Informe ao usuário e encerre o programa;
• Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
informe-a ao usuário;
• Se o delta for positivo, a equação possui duas raízes reais; informe-as ao
usuário;
'''

a = float(input("Informe o valor de 'a': "))
if a == 0:
    print("O valor de 'a' não pode ser igual a 0!")
    exit(0)

b = float(input("Informe o valor de 'b': "))
c = float(input("Informe o valor de 'c': "))
delta = b ** - (4 * a * c) #algo de errado nessa equação...
x1 = (-b + delta) / 2 * a
x2 = (-b - delta) / 2 * a

print("O valor do delta é: " + str(delta))
if delta < 0:
    print("A equação não possui raízes reais!")
    exit(0)
elif delta == 0:
    print("A equação possui apenas uma raíz real: ")
    print("x = " + str(x2))
elif delta > 0:
    print("A equação possui duas raízes reais: ")
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))