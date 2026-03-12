'''
Um pescador paga multa de R$4,00 por quilo excedente caso ultrapasse 50 kg de peixes. Faça
um programa que calcule excesso e multa.
'''

peixe = float(input("Insira quantos kg de peixe você quer levar: "))
valorPeixe = peixe * 20

if peixe > 50:
    peixeExcedente = peixe - 50
    valorMulta = 4 * peixeExcedente
    valorTotal = valorPeixe + valorMulta
    print("Você está levando " + str(peixeExcedente) + " kg de peixe a mais! Multa de " + str(valorMulta) + " aplicada.")
    print("Você está levando " + str(peixe) + " kg de peixe. O valor total a ser pago é igual a " + str(valorTotal))
else:
    print("Você está levando " + str(peixe) + " kg de peixe. O valor total a ser pago é igual a " + str(valorPeixe))