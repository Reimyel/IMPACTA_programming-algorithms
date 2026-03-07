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
quantidadeHoras = float(input("Informe quantas horas você trabalha: "))
salarioBruto = ""
descontoIR = ""
descontoINSS = 10 / 100 * salarioBruto
valorFGTS = 11 / 100 * salarioBruto
totalDescontos = salarioBruto - descontoIR - descontoINSS
salarioLiquido = ""

if salarioBruto <= 900:
    print(salarioBruto)
    print(descontoIR)
    print(descontoINSS)
    print(valorFGTS)
    print(totalDescontos)
    print(salarioLiquido)

else:
    print("Erro inesperado...")

print("Seu salário atual é igual a: R$ " + str())
print("O porcentual de aumento que será aplicado é de: " + str())
print("O aumento do seu salário será de: " + str())
print("Seu salário após os reajustes será igual a: R$ " + str())