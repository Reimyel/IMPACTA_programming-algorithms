def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

numeroInput = input("Digite um número inteiro positivo: ")
print(f"O fatorial de {numeroInput} é igual a {calcular_fatorial(int(numeroInput))}")