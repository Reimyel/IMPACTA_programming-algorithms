def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for i in texto:
        if i in vogais:
            contador += 1
    return contador

textoInput = input("Digite um texto: ")
print(f"Seu texto tem {contar_vogais(textoInput)} vogais")