'''
Exercício 1: Função Afim (Custo de Serviço) - Nível Médio
Contexto ENEM: Uma empresa de telefonia cobra uma taxa fixa de R$ 20,00
mais R$ 0,50 por minuto de ligação. Crie uma função em Python que receba a
quantidade de minutos e retorne o valor total da fatura. Construa a Fluxograma
'''

def calcular_fatura(minutos):
    taxa_fixa = 20.00
    custo_minuto = 0.50
    valor_total = taxa_fixa + (custo_minuto * minutos)
    return valor_total

minutosInput = float(input("Digite a quantidade de minutos de ligação: "))
fatura = calcular_fatura(minutosInput)
print(f"O valor total da fatura é: R$ {fatura:.2f}")