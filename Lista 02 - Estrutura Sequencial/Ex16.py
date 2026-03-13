'''
Uma loja de tintas precisa calcular quantas latas comprar. 1 litro cobre 3 m2, lata tem 18 litros e
custa R$80.
'''

area = float(input("Informe quantos metros quadrados deseja cobrir com tinta: "))
latas = int(area / (3 * 18))
custo = 80 * latas

print("Você precisa comprar " + str(latas) + " lata(s) de tinta. O preço total é " + str(custo) + ".")