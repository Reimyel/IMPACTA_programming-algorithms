def calcular_media(notas):
    r = sum(notas) / len(notas)
    return r

notasInput = input("Digite suas notas separadas por espaços: ")
listaNotas = notasInput.split()

print(calcular_media(listaNotas))