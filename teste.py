RA = input("Digite seu RA: ")

if len(RA) == 7:
    for n in RA:
        arquivo = open(f"{n}.txt", "w")
        arquivo.write(f"{n}")
else:
    print("Erro")