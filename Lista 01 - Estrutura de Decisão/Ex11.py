'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para 
desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e 
o reajuste segundo o seguinte critério, baseado no salário atual:
• salários até R$ 280,00 (incluindo) : aumento de 20%
• salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
• salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
• salários de R$ 1500,00 em diante : aumento de 5%
Após o aumento ser realizado, informe na tela:
• o salário antes do reajuste;
• o percentual de aumento aplicado;
• o valor do aumento;
• o novo salário, após o aumento.
'''

salarioAtual = float(input("Informe seu salário: "))
percentualAumento = ""
valorAumento = ""
salarioReajuste = ""

if salarioAtual <= 280:
    percentualAumento = 20
    valorAumento = percentualAumento / 100 * salarioAtual
    salarioReajuste = salarioAtual + valorAumento

elif salarioAtual > 280 and salarioAtual <= 700:
    percentualAumento = 15
    valorAumento = percentualAumento / 100 * salarioAtual
    salarioReajuste = salarioAtual + valorAumento

elif salarioAtual > 700 and salarioAtual <= 1500:
    percentualAumento = 10
    valorAumento = percentualAumento / 100 * salarioAtual
    salarioReajuste = salarioAtual + valorAumento

elif salarioAtual > 1500:
    percentualAumento = 5
    valorAumento = percentualAumento / 100 * salarioAtual
    salarioReajuste = salarioAtual + valorAumento
    
else:
    print("Erro inesperado...")

print("Seu salário atual é igual a: R$ " + str(salarioAtual))
print("O porcentual de aumento que será aplicado é de: " + str(percentualAumento))
print("O aumento do seu salário será de: " + str(valorAumento))
print("Seu salário após os reajustes será igual a: R$ " + str(salarioReajuste))