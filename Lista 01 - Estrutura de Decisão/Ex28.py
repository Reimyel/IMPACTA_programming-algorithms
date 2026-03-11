'''
O Hipermercado Tabajara está com uma promoção de carnes que é
imperdível. Confira:
• File Duplo: Até 5 Kg -> R$ 4,90 por Kg | Acima de 5 Kg -> R$ 5,80 por Kg
• Alcatra: Até 5 Kg -> R$ 5,90 por Kg | Acima de 5 Kg -> R$ 6,80 por Kg
• Picanha: Até 5 Kg -> R$ 6,90 por Kg | Acima de 5 Kg -> R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos
de carne da promoção, porém não há limites para a quantidade de carne por
cliente. Se a compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e
a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo
as informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar.
'''

print("F - Filé Duplo\nA - Alcatra\nP - Picanha")
carne = str(input("Qual carne quer comprar? Informe apenas a inícial, como demonstrado acima: ")).lower()
if carne == "f":
    tipoCarne = "Filé Duplo"
elif carne == "a":
    tipoCarne = "Alcatra"
elif carne == "p":
    tipoCarne = "Picanha"
else:
    print("Opção inválida!")
    exit(0)
#
print("C - Crédito\nD - Débito\nP - Pix\nT - Cartão Tabajara (5% OFF)")
pagamento = str(input("Que forma de pagamento deseja usar?: ")).lower()
if pagamento == "c":
    formaPagamento = "Crédito"
elif pagamento == "d":
    formaPagamento = "Débito"
elif pagamento == "p":
    formaPagamento = "Pix"
elif pagamento == "t":
    formaPagamento = "Cartão Tabajara"
else:
    print("Opção inválida!")
    exit(0)
#
quantia = float(input("Quantos Kg de carne quer comprar?: "))
if tipoCarne == "Filé Duplo":
    if quantia <= 5:
        filePreco = 4.9 * quantia
    else:
        filePreco = 5.8 * quantia
    
    desconto = (5 / 100) * filePreco
    if formaPagamento == "Cartão Tabajara":
        precoTotal = filePreco - desconto
    else:
        precoTotal = filePreco

    print("\nTipo de Carne: " + tipoCarne + "\n" + "Quantia: " + str(quantia) + "\n" + "Preço: " + str(filePreco) + "\n" + "Forma de Pagamento: " + formaPagamento + "\n" + "Desconto: " + str(desconto) + "\n" + "Preço Total: " + str(precoTotal))
elif tipoCarne == "Alcatra":
    if quantia <= 5:
        alcatraPreco = 5.9 * quantia
    else:
        alcatraPreco = 6.8 * quantia

    desconto = (5 / 100) * alcatraPreco
    if formaPagamento == "Cartão Tabajara":
        precoTotal = alcatraPreco - desconto
    else:
        precoTotal = alcatraPreco

    print("\nTipo de Carne: " + tipoCarne + "\n" + "Quantia: " + str(quantia) + "\n" + "Preço: " + str(alcatraPreco) + "\n" + "Forma de Pagamento: " + formaPagamento + "\n" + "Desconto: " + str(desconto) + "\n" + "Preço Total: " + str(precoTotal))
else:
    if quantia <= 5:
        picanhaPreco = 6.9 * quantia
    else:
        picanhaPreco = 7.8 * quantia

    desconto = (5 / 100) * picanhaPreco
    if formaPagamento == "Cartão Tabajara":
        precoTotal = picanhaPreco - desconto
    else:
        precoTotal = picanhaPreco

    print("\nTipo de Carne: " + tipoCarne + "\n" + "Quantia: " + str(quantia) + "\n" + "Preço: " + str(picanhaPreco) + "\n" + "Forma de Pagamento: " + formaPagamento + "\n" + "Desconto: " + str(desconto) + "\n" + "Preço Total: " + str(precoTotal))

