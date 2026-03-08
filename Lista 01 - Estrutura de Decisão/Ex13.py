'''
Faça um programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se 
digitar outro valor deve aparecer valor inválido.
'''

num = int(input("Digite um número de 1 a 7: "))

match num:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("Número Inválido!")