def calcular_media(ap1, ap2, ap3):
    apFinal = (float(ap1) + float(ap2) + float(ap3)) / 3
    return apFinal

ap1Input = input("Digite sua primeira nota: ")
ap2Input = input("Digite sua segunda nota: ")
ap3Input = input("Digite sua terceira nota: ")

print(f"Sua nota final é {calcular_media(ap1Input, ap2Input, ap3Input):.2f}")