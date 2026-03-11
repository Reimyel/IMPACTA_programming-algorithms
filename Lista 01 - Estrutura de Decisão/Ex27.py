'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
• Morango: Até 5 Kg -> R$ 2,50 por Kg | Acima de 5 Kg -> R$ 2,20 por Kg
• Maçã: Até 5 Kg -> R$ 1,80 por Kg | Acima de 5 Kg -> R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar
R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um
algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de
maçãs adquiridas e escreva o valor a ser pago pelo cliente.
'''

morango = float(input("Quantos Kg de morangos quer comprar?: "))
maca = float(input("Quantas Kg maçãs quer comprar?: "))
frutas = morango + maca
#morango
if morango <= 5:
    morangoPreco = 2.5 * morango
else:
    morangoPreco = 2.2 * morango

#maça
if maca <= 5:
    macaPreco = 1.8 * maca
else:
    macaPreco = 1.5 * maca

totalPreco = morangoPreco + macaPreco

if frutas >= 8 or totalPreco > 25:
    desconto = (10 / 100) * totalPreco
    totalPreco -= desconto
    print("Sua compra possui 10% de desconto! O total da compra é: " + str(totalPreco))
else:
    print("O total da compra é: " + str(totalPreco))