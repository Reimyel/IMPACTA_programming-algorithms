'''
Faça um programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo. Observando
os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
• 326 = 3 centenas, 2 dezenas e 6 unidades
• 12 = 1 dezena e 2 unidades
'''
num = int(input("Digite um número inteiro menor que 1000: "))
numString = str(num)

if num < 10:
    unidade = numString[0]
    print(numString + " = " + unidade + " unidade(s)")
elif num < 100:
    dezena = numString[0]
    unidade = numString[1]
    print(numString + " = " + dezena + " dezena(s) e " + unidade + " unidade(s)")
elif num < 1000:
    centena = numString[0]
    dezena = numString[1]
    unidade = numString[2]
    print(numString + " = " + centena + " centena(s), " + dezena + " dezena(s) e " + unidade + " unidade(s)")
else:
    print("Número inválido!")