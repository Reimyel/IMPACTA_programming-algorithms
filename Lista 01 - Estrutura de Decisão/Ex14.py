'''
Faça um programa que lê as duas notas parciais obtidas por um
aluno numa disciplina ao longo de um semestre, e calcule a sua média. A
atribuição de conceitos obedece à tabela abaixo:
• Entre 9.0 e 10.0 -> A
• Entre 7.5 e 9.0 -> B
• Entre 6.0 e 7.5 -> C
• Entre 4.0 e 6.0 -> D
• Entre 4.0 e zero -> E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o
conceito for D ou E.
'''

notaParcial1 = float(input("Digite sua primeira nota parcial do semestre: "))
notaParcial2 = float(input("Digite sua segunda nota parcial do semestre: "))
media = (notaParcial1 + notaParcial2) / 2

if media <= 4:
    notaFinal = "E"
elif media <= 6:
    notaFinal = "D"
elif media <= 7.5:
    notaFinal = "C"
elif media <= 9:
    notaFinal = "B"
elif media <= 10:
    notaFinal = "A"
else:
    print("Nota Inválida!")
    exit

print("Nota Parcial 1: " + str(notaParcial1))
print("Nota Parcial 2: " + str(notaParcial2))
print("Média Final: " + str(media))

if notaFinal == "A" or notaFinal == "B" or notaFinal == "C":
    print("APROVADO")
else:
    print("REPROVADO")