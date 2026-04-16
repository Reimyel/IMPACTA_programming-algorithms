def configurar_perfil(nome, idade, cidade="Desconhecida"):
    print(f"Seu nome: {nome}\nSua idade: {idade}\nSua cidade: {cidade}")

nomeInput = str(input("Informe seu nome: "))
idadeInput = int(input("Informe sua idade: "))
cidadeInput = str(input("Informe sua cidade: "))
configurar_perfil(nomeInput, idadeInput)