def maior_valor(a, b):
    return a if float(a) > float(b) else b

valorA = input("Digite o primeiro número: ")
valorB = input("Digite o segundo número: ")

print(f"{maior_valor(valorA, valorB)} é o maior número")