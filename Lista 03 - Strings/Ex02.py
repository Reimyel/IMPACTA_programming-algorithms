'''
Nome ao contrário em maiúsculas: Leia o nome do usuário e mostre-o de trás para frente em
letras maiúsculas.
'''

nome = str(input("Informe seu nome: "))
nomeReverso = nome[::-1]
                   
print(nomeReverso.upper())