'''
Corrigir telefone: Leia um telefone com 7 ou 8 dígitos e ajuste adicionando o '3' se necessário.
'''

telefoneBruto = input("Digite seu telefone: ")

telefoneLimpo = telefoneBruto.replace("-", "")

tamanho = len(telefoneLimpo)

if tamanho == 7:
    print("Telefone possui 7 dígitos. Vou adicionar o 3 na frente.")
    telefoneFinal = "3" + telefoneLimpo
elif tamanho == 8:
    telefoneFinal = telefoneLimpo
else:
    telefoneFinal = "Número fora do padrão (não tem 7 nem 8 dígitos)"

print(f"Telefone corrigido: {telefoneFinal}")