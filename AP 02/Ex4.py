'''
4. Questão 4: Contagem de Palavras em Arquivos (Manipulação de Arquivos e
Strings)
Habilidade Avaliada: Persistência de dados em arquivos de texto e
normalização de cadeias de caracteres (strings).
Fundamentação Lógica: A solução requer o gerenciamento seguro de
recursos externos.
    1. Manipulação de Arquivo: O uso da instrução with open(...) é o padrão
    esperado para garantir o fechamento do arquivo mesmo em caso de
    exceções.
    2. Tratamento de Strings: A normalização através do método .lower() é
    essencial para o processamento case-insensitive.
    3. Precisão da Contagem: O uso do método .split() transforma o conteúdo
    em uma lista de palavras isoladas. Isso evita erros comuns de contagem
    por substring (ex: encontrar a palavra "voto" dentro de "votos"),
    garantindo que apenas tokens idênticos à palavra de busca sejam
    computados.
Padrão de Resposta Esperado:
palavra_alvo = input("Digite a palavra a ser buscada: ").lower()
with open("votos.txt", "r") as arquivo:
conteudo =
Palavras =
Total =
print("A palavra '%s' foi encontrada %d vezes." % (palavra_alvo, total))
'''

palavra_alvo = input("Digite a palavra a ser buscada: ").lower()
with open("Tipo.txt", "r") as arquivo:
    conteudo = arquivo.read().lower()
    palavras = conteudo.split()
    total = palavras.count(palavra_alvo)
    print("A palavra '%s' foi encontrada %d vezes." % (palavra_alvo, total))