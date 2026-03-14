'''
Data por extenso: Leia uma data (dd/mm/aaaa) e mostre no formato '29 de Outubro de 1973'.
'''

data = str(input("Escreva uma data no formato dd/mm/aaaa: "))
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
partes = data.split("/")

dia = int(partes[0])
mesNum = int(partes[1])
mesExt = meses[mesNum]
ano = partes[2]

print(f"{dia} de {mesExt} de {ano}")