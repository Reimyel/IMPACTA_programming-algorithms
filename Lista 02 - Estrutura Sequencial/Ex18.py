'''
Faça um programa que calcule o tempo aproximado de download de um arquivo dado seu
tamanho (MB) e velocidade da internet (Mbps).
'''

arquivoMB = float(input("Informe o tamanho do seu arquivo em MB: "))
velInternetMbps = float(input("Informe a velocidade da sua internet em Mbps: "))
tempoSegundos = (arquivoMB * 8) / velInternetMbps
tempoMinutos = tempoSegundos / 60

print(f"O tempo aproximado de download do seu arquivo é {tempoMinutos:.2f} minutos")