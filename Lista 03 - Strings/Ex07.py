'''
Contar espaços e vogais: Dada uma frase, conte quantos espaços existem e quantas vezes
aparecem as vogais.
'''

frase = str(input("Informe uma frase: "))
vogais = "aeiouAEIOU"
espacosFrase = 0
vogaisFrase = 0
for letra in frase:
    if letra == " ":
        espacosFrase += 1

    if letra in vogais:
        vogaisFrase += 1

print(f"Sua frase tem {espacosFrase} espaços e {vogaisFrase} vogais.")