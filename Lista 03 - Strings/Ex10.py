'''
Número por extenso: Leia um número até 99 e mostre-o por extenso.
'''

numero = int(input("Insira um número de 0 a 99: "))

unidades = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove")
especiais = ("dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezesete", "dezoito", "dezenove")
dezenas = ("", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa")

if numero < 10:
    print(unidades[numero])
elif 10 <= numero <= 19:
    print(especiais[numero - 10])
else:
    d = numero // 10
    u = numero % 10
    if u == 0:
        print(dezenas[d])
    else:
        print(dezenas[d] + " e " + unidades[u])