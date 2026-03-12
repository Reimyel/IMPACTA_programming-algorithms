'''
Peça dois números inteiros e um número real. Calcule: (a) o produto do dobro do primeiro com
metade do segundo; (b) a soma do triplo do primeiro com o terceiro; (c) o terceiro elevado ao cubo.
'''

numInt1 = int(input("Informe um número inteiro: "))
numInt2 = int(input("Informe outro número inteiro: "))
numReal = float(input("Informe um número real: "))
casoA = (numInt1*2) * (numInt2/2)
casoB = (numInt1*3) + numReal
casoC = numReal**3

print(casoA)
print(casoB)
print(casoC)