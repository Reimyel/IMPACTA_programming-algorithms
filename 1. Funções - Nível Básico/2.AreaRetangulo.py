def calcular_area(base, altura):
    area = float(base) * float(altura)
    return area

baseInput = input("Digite a base do seu retângulo: ")
alturaInput = input("Digite a altura do seu retângulo: ")

print(f"A área do seu retângulo é {calcular_area(baseInput, alturaInput)}")