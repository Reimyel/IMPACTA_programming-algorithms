'''
Faça um programa que pergunte em que turno você estuda. Peça para digitar:
• M - Matutino
• V - Vespertino
• N - Noturno
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

turno = str(input("Em qual turno você estuda? Matutino, Vespertino ou Noturno? Digite M, V ou N respectivamente:\n"))

match turno:
    case "M":
        print("Bom Dia!")
    case "V":
        print("Boa Tarde!")
    case "N":
        print("Boa Noite!")
    case _:
        print("Valor Inválido!")