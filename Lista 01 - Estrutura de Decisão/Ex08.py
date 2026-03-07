'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a 
decisão é sempre pelo mais barato.
'''

custoProduto1 = float(input("Digite o preço do primeiro produto: "))
custoProduto2 = float(input("Digite o preço do primeiro produto: "))
custoProduto3 = float(input("Digite o preço do primeiro produto: "))

if ((custoProduto1 < custoProduto2) and (custoProduto1 < custoProduto3)):
    print("Recomendamos que compre o primeiro produto, cujo preço é R$ " + str(custoProduto1))
elif ((custoProduto2 < custoProduto1) and (custoProduto2 < custoProduto3)):
    print("Recomendamos que compre o segundo produto, cujo preço é R$ " + str(custoProduto2))
elif ((custoProduto3 < custoProduto1) and (custoProduto3 < custoProduto2)):
    print("Recomendamos que compre o terceiro produto, cujo preço é R$ " + str(custoProduto3))
else:
    print("Todos os produtos possuem o mesmo preço!")