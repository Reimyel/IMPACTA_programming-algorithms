'''
Faça um programa que peça os 3 lados de um triângulo. O programa
deverá informar se os valores podem ser um triângulo. Indique, caso os lados
formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
• Três lados formam um triângulo quando a soma de quaisquer dois lados for
maior que o terceiro;
• Triângulo Equilátero: três lados iguais;
• Triângulo Isósceles: quaisquer dois lados iguais;
• Triângulo Escaleno: três lados diferentes;
'''

ladoTriangulo1 = float(input("Informe o primeiro lado do triângulo: "))
ladoTriangulo2 = float(input("Informe o segundo lado do triângulo: "))
ladoTriangulo3 = float(input("Informe o terceiro lado do triângulo: "))

if ((ladoTriangulo1 + ladoTriangulo2) > ladoTriangulo3) or ((ladoTriangulo1 + ladoTriangulo3) > ladoTriangulo2):
    triangulo = True
elif ((ladoTriangulo2 + ladoTriangulo1) > ladoTriangulo3) or ((ladoTriangulo2 + ladoTriangulo3) > ladoTriangulo1):
    triangulo = True
elif ((ladoTriangulo3 + ladoTriangulo1) > ladoTriangulo2) or ((ladoTriangulo3 + ladoTriangulo2) > ladoTriangulo1):
    triangulo = True
else:
    triangulo = False
    print("Você não tem um triângulo!")
    exit

if triangulo == True:
    if ladoTriangulo1 == ladoTriangulo2 == ladoTriangulo3:
        print("Seu triângulo é equilátero! Ele tem três lados iguais")
    elif ((ladoTriangulo1 == ladoTriangulo2) or (ladoTriangulo1 == ladoTriangulo3)) or ((ladoTriangulo2 == ladoTriangulo1) or (ladoTriangulo2 == ladoTriangulo3)) or ((ladoTriangulo3 == ladoTriangulo1) or (ladoTriangulo3 == ladoTriangulo2)):
        print("Seu triângulo é isósceles! Ele tem dois lados iguais")
    else:
        print("Seu triângulo é escaleno! Ele tem três lados diferentes")