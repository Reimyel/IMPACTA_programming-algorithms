'''
Palavra embaralhada: Mostre uma palavra com letras embaralhadas e permita que o usuário
adivinhe.
'''

palavraCorrigida = "ALGORITMO"
letras = list(palavraCorrigida)
tamanho = len(letras)

for i in range(tamanho):
    novoIndice = (i + 3) % tamanho
    
    aux = letras[i]
    letras[i] = letras[novoIndice]
    letras[novoIndice] = aux

palavraEmbrulhada = "".join(letras)

print(f"A palavra embaralhada é: {palavraEmbrulhada}")
tentativas = 3

while tentativas > 0:
    chute = input("Qual é a palavra original? ").upper()
    if chute == palavraCorrigida:
        print("Parabéns! Você acertou.")
        break
    else:
        tentativas -= 1
        print(f"Errado! Você tem {tentativas} tentativas.")