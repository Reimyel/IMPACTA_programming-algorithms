'''
Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
• F - Feminino
• M - Masculino
• Sexo Inválido.
'''

letra = str(input("Digite uma letra: "))

match letra:
    case "M":
        print("Masculino")
    case "F":
        print("Feminino")
    case _:
        print("Sexo Inválido!")