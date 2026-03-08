'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que 
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do 
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto 
menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas 
no mês.
Desconto do IR:
• Salário Bruto até 900 (inclusive) - isento
• Salário Bruto até 1500 (inclusive) - desconto de 5%
• Salário Bruto até 2500 (inclusive) - desconto de 10%
• Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a 
quantidade de hora é 220.
• Salário Bruto: (5 * 220) : R$ 1100,00
• (-) IR (5%) : R$ 55,00
• (-) INSS ( 10%) : R$ 110,00
• FGTS (11%) : R$ 121,00
• Total de descontos : R$ 165,00
• Salário Liquido : R$ 935,00
'''

valorHora = float(input("Informe o valor da sua hora: "))
quantidadeHoras = float(input("Informe quantas horas você trabalha por mês: "))
salarioBruto = valorHora * quantidadeHoras
if salarioBruto <= 900:
    valorIR = 0
elif salarioBruto <= 1500:
    valorIR = 5
elif salarioBruto <= 2500:
    valorIR = 10
elif salarioBruto > 2500:
    valorIR = 20
else:
    print("Erro inesperado...")
    exit

descontoIR = valorIR / 100 * salarioBruto
descontoINSS = 10 / 100 * salarioBruto
valorFGTS = 11 / 100 * salarioBruto
totalDescontos = descontoIR + descontoINSS
salarioLiquido = salarioBruto - descontoIR - descontoINSS

print("\nSalário Bruto: (5 * 220) : R$ " + str(salarioBruto))
print("(-) IR (5%) : R$ " + str(descontoIR))
print("(-) INSS ( 10%) : R$ " + str(descontoINSS))
print("FGTS (11%) : R$ " + str(valorFGTS))
print("Total de descontos : R$ " + str(totalDescontos))
print("Salário Liquido : R$ " + str(salarioLiquido))