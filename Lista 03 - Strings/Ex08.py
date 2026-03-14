'''
Palíndromo: Leia uma sequência de caracteres e informe se é um palíndromo.
'''

palavra = str(input("Informe uma sequência de caracteres (sem acentuação): "))
palavraReversa = palavra[::-1]
pSemEspaco = palavra.replace(" ", "")
prvsSemEspaco = palavra.replace(" ", "")

if pSemEspaco == prvsSemEspaco:
    print("Sua sequência é um palíndromo!")
else:
    print("Sua sequência não é um palíndromo!")