'''
Faça um programa para leitura de três notas parciais de um aluno. O
programa deve calcular a média alcançada por aluno e apresentar:
• A mensagem "Aprovado", se a média for maior ou igual a 7, com a
respectiva média alcançada;
• A mensagem "Reprovado", se a média for menor do que 7, com a respectiva
média alcançada;
• A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

notaParcial1 = float(input("Digite sua primeira nota parcial do semestre: "))
notaParcial2 = float(input("Digite sua segunda nota parcial do semestre: "))
notaParcial3 = float(input("Digite sua terceira nota parcial do semestre: "))
media = (notaParcial1 + notaParcial2 + notaParcial3) / 3

print("Média Final: " + str(media))

if media == 10:
    print("APROVADO COM DISTINÇÃO")
elif media >= 7:
    print("APROVADO")
elif media < 7:
    print("REPROVADO")
else:
    print("NOTA INVÁLIDA")