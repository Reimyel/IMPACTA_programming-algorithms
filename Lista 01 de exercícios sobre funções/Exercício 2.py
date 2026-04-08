'''
Exercício 2: Cálculo de Imposto (Funções com Retorno)

Objetivo: Praticar funções que realizam cálculos matemáticos e retornam
resultados para o programa principal.

Enunciado: Crie uma função chamada soma_imposto que possua dois
parâmetros:
    1. taxa_imposto: a quantia de imposto sobre vendas expressa em
porcentagem (ex: 10 para 10%).
    2. custo: o valor de um item antes do imposto.
A função deve calcular o valor final do produto (custo + imposto) e retornar esse
novo valor. Em seguida, peça ao usuário que digite o custo e a taxa, chame a
função e imprima o resultado com duas casas decimais.
'''

def soma_imposto(taxa_imposto, custo):
    valor_final_produto = custo + taxa_imposto
    return valor_final_produto

inputCusto = input("Digite o custo do produto: ")
inputTaxa = input("Digite a taxa imposta a esse produto: ")
resultado = soma_imposto(int(inputTaxa), int(inputCusto))
print("O valor final do seu produto é " + f"{resultado:.2f}")