def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
numInput = input("Digite um número inteiro positivo: ")
print(fibonacci(int(numInput)))