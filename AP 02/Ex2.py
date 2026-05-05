'''
Exercício 2: Função Quadrática (Área/Produção) - Nível Difícil
Contexto ENEM: A produção de uma fábrica segue a função \(P(x) = -x^2 +
10x + 50\), onde \(x\) é o número de máquinas. Crie uma função que receba
\(x\) e retorne a produção. Além disso, a função deve retornar 0 se o número de
máquinas for negativo. Construa a Fluxograma
'''

def calcular_producao(x):
    if x < 0:
        return 0
    else:
        producao = (-x)**2 + 10*x + 50
        return producao
    
maquinasInput = int(input("Digite o número de máquinas na sua empresa: "))
producao = calcular_producao(maquinasInput)
print(f"A produção total da sua empresa é: {producao:.2f}")