'''
Versão avançada da tinta: 1 litro cobre 6 m2. Lata 18L (R$80) e galão 3,6L (R$25). Calcular
melhor opção com 10% de folga.
'''

area = float(input("Informe quantos metros quadrados deseja cobrir com tinta: "))
areaFolga = area * 1.1
restoArea = areaFolga % (6 * 18)
latas = int(area // (6 * 18))
custoLatas = 80 * latas
galao = area / (6 * 3.6)
custoGalao = 25 * galao

if restoArea > 0:
    print("Você precisa comprar " + str(latas) + " lata(s) e 1 galão de tinta. O preço total é " + str(custoLatas) + str(custoGalao) + ".")
else:
    print("Você precisa comprar " + str(latas) + " lata(s) de tinta. O preço total é " + str(custoLatas) + ".")