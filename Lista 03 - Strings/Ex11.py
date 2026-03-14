'''
Jogo da Forca: Desenvolva um jogo simples da forca usando uma lista de palavras.
'''

palavraSecreta = "DESAFIO"
letrasDescobertas = ["_"] * len(palavraSecreta)
tentativas = 6
letrasErradas = ""

while tentativas > 0 and "_" in letrasDescobertas:
    print("Palavra:", " ".join(letrasDescobertas))
    print(f"Tentativas: {tentativas} | Erros: {letrasErradas}")
    
    chute = input("Chute uma letra: ").upper()

    if chute in palavraSecreta:
        indice = 0
        for letra in palavraSecreta:
            if letra == chute:
                letrasDescobertas[indice] = chute
            indice += 1
    else:
        if chute not in letrasErradas:
            letrasErradas += chute + " "
            tentativas -= 1