'''
Escada invertida: Mostre o nome em escada decrescente.
'''

nome = str(input("Informe seu nome: "))

for letra in range(len(nome), 0, -1):
    print(nome[:letra])