'''
Faça um programa para um caixa eletrônico. O programa deverá
perguntar ao usuário o valor do saque e depois informar quantas notas de cada
valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O
valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se
preocupar com a quantidade de notas existentes na máquina.
• Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
• Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três
notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro
notas de 1.
'''

print("BEM VINDO AO CAIXA ELETRÔNICO")
saque = int(input("Informe um valor inteiro para saque de 10 a 600: "))

if saque >= 10 and saque <= 600:
    centena = int(saque / 100)
    #REDUÇÃO DO SAQUE
    saque = saque - (centena * 100)

    cinquenta = int(saque / 50)
    #REDUÇÃO DO SAQUE
    saque = saque - (cinquenta * 50)

    dezena = int(saque / 10)
    #REDUÇÃO DO SAQUE
    saque = saque - (dezena * 10)

    cinco = int(saque / 5)
    #REDUÇÃO DO SAQUE
    saque = saque - (cinco * 5)

    unidade = saque
    print(str(centena) + " nota(s) de 100, " + str(cinquenta) + " nota(s) de 50, " + str(dezena) + " nota(s) de 10, " + str(cinco) + " nota(s) de 5 e " + str(unidade) + " nota(s) de 1.")
else:
    print("SAQUE NÃO AUTORIZADO. INFORME UMA QUANTIA INTEIRA ENTRE 10 E 600 REAIS.")