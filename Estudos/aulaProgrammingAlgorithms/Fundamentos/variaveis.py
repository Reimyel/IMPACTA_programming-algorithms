nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 0.12345678910

dados = {"nome": "Guilherme", "idade": 28}

#print("Nome: %s Idade: %d" % (nome, idade))
#print("Nome: {} Idade: {}".format(nome, idade))
#print("Nome: {1} Idade: {0}".format(idade, nome))
#print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

#print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
#print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.9f}")