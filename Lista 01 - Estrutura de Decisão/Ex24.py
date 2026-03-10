'''
Faça um programa que leia 2 números e em seguida pergunte ao
usuário qual operação ele deseja realizar. O resultado da operação deve ser
acompanhado de uma frase que diga se o número é:
• par ou ímpar;
• positivo ou negativo;
• inteiro ou decimal.
'''

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

operacao = str(input("Qual operação deseja realizar?\nDigite SUM para SOMA, SUB para SUBTRAÇÃO, MULT para MULTIPLICAÇÃO ou DIV para DIVISÃO:\n"))

match operacao:
    case "SUM":
        result = num1 + num2
    case "SUB":
        result = num1 - num2
    case "MULT":
        result = num1 * num2
    case "DIV":
        result = num1 / num2
    case _:
        print("Operação inválida!")
        exit(0)

print("O resultado da sua operação é: " + str(result))

resultMod = result % 2
if resultMod == 0:
    print("Seu resultado é par")
else:
    print("Seu resultado é impar")

if result > 0:
    print("Seu resultado é positivo")
else:
    print("Seu resultado é negativo")

resultArrd = round(result)
if result == resultArrd:
    print("Seu resultado é inteiro")
else:
    print("Seu resultado é decimal")