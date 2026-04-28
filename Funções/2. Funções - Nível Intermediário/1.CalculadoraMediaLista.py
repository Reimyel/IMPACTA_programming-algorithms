def calcular_media(notas):
    r = sum(notas) / len(notas)
    return r

notasInput = input("Digite suas notas separadas por espaços: ")
listaNotas = notasInput.split()

listaNotas = [float(nota) for nota in listaNotas]

print(f"Sua nota final é {calcular_media(listaNotas):.2f}")