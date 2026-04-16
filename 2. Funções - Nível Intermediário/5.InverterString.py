def inverter_string(texto):
    textoInvertido = texto[::-1]
    return textoInvertido

textoInput = input("Digite um texto: ")
print(f"O texto {textoInput} se torna {inverter_string(textoInput)} quando invertido")