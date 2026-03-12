'''
Converta um valor em Gigabytes para Megabytes e Kilobytes.
'''

gb = float(input("Informe um valor de Megabytes: "))
mb = gb * 1024
kb = gb * 1000000

print("Seu valor em Gigabytes é igual a " + str(mb))
print("Seu valor em Kilobytes é igual a " + str(kb))