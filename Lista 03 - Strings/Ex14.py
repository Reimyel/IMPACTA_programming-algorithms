'''
Leet Speak: Leia um texto e converta para a escrita estilo leet (ex: 1337).
'''

tabela = {
    'A': '4',
    'E': '3',
    'I': '1',
    'O': '0',
    'S': '5',
    'T': '7'
}

frase = input("Digite o texto: ").upper()
resultado = ""

for letra in frase:
    if letra in tabela:
        resultado += tabela[letra]
    else:
        resultado += letra

print(f"Texto Leet: {resultado}")