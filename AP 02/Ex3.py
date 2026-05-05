'''
Exercício 3: Análise de Estrutura (Estilo Concurso/ENEM)
Analise o código abaixo e determine o resultado final para as entradas
fornecidas:
'''

def verificar_nivel(valor):
    if valor < 0:
        return "Negativo"
    elif valor < 10:
        return "Baixo"
    else:
        return "Alto"
    

print(verificar_nivel(5)) #Print 1
print(verificar_nivel(15)) #Print 2
print(verificar_nivel(-1)) #Print 3

'''
Respostas:
- Print 1 retorna "Baixo", pois 5 é menor que 10 e não é negattivo
- Print 2 retorna "Alto", pois 15 é maior que 10
- Print 3 retorna "Negativo", pois -1 é menor que 0
'''