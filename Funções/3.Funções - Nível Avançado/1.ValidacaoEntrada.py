def leia_int(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print("Entrada inválida, digite um número inteiro")
    
    

intInput = leia_int("Digite um número inteiro: ")
print(intInput)