def verificar_par(numero):
    sobra = float(numero) % 2
    return True if float(sobra) == 0 else False

numeroInput = input("Digite um número: ")

print(f"Seu número é par? {verificar_par(numeroInput)}")