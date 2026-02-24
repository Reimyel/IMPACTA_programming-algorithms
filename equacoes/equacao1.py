x = int(input("Digite um número inteiro: "))

resultado = x + 2 * x

if x >= 0:
    print(f"O número é {x}, e seu dobro é {2 * x}.\nSomados, o resultado é {resultado}.")

elif x < 0:
    print("Número negativo não aceito!")

else:
    print("Número não aceito...")