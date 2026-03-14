'''
Nome em escada: Mostre o nome em formato de escada crescente (F, FU, FUL...).
'''

nome = str(input("Informe seu nome: "))

for letra in range(1, len(nome) + 1):
    print(nome[0:letra])