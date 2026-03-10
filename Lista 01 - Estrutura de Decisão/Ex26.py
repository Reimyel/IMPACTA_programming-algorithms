'''
Um posto está vendendo combustíveis com a seguinte tabela de
descontos:
• Álcool:
o até 20 litros: desconto de 3% por litro
o acima de 20 litros: desconto de 5% por litro
• Gasolina:
o até 20 litros: desconto de 4% por litro
o acima de 20 litros: desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a
ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 e o
preço do litro do álcool é R$ 1,90.
'''
print("A - Álcool\nG - Gasolina")
combustivel = str(input("Qual combustível quer comprar? Informe apenas a inícial, como demonstrado acima: ")).lower()
if combustivel == "a":
    tipoCombustivel = "Álcool"
elif combustivel == "g":
    tipoCombustivel = "Gasolina"
else:
    print("Opção inválida!")
    exit(0)

litros = float(input("Quantos litros de combustível quer comprar?: "))
if tipoCombustivel == "Álcool":
    if litros <= 20:
        desconto = (3 / 100) * litros
    else:
        desconto = (5 / 100) * litros
    
    precoAlc = (litros * 1.90) - desconto
    print(precoAlc)
else:
    if litros <= 20:
        desconto = (4 / 100) * litros
    else:
        desconto = (6 / 100) * litros
    
    precoGas = (litros * 2.50) - desconto
    print(precoGas)