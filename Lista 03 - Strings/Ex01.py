'''
Tamanho de strings: Leia duas strings, mostre o conteúdo e o tamanho de cada uma. Informe se
possuem o mesmo tamanho e se o conteúdo é igual ou diferente.
'''

palavra1 = input("Escreva uma palavra: ")
palavra2 = input("Escreva outra palavra: ")
if len(palavra1) == len(palavra2):
    print("O tamanho de ambas as palavras é igual!")

if palavra1 == palavra2:
    print("O conteúdo de ambas as palavras é igual!")