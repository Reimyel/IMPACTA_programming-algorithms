'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um
crime. As perguntas são:
1. "Telefonou para a vítima?"
2. "Esteve no local do crime?"
3. "Mora perto da vítima?"
4. "Devia para a vítima?"
5. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa
no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
'''

pontos = int()
p1 = str(input("Telefonou para a vítima?\n")).lower()
if p1 == "sim":
    pontos += 1
    print("Suspeito, próxima pergunta...")
elif p1 == "não":
    print("Certo, próxima pergunta...")
else:
    print("Resposta inválida!")
    exit(0)
p2 = str(input("Esteve no local do crime?\n")).lower()
if p2 == "sim":
    pontos += 1
    print("Suspeito, próxima pergunta...")
elif p2 == "não":
    print("Certo, próxima pergunta...")
else:
    print("Resposta inválida!")
    exit(0)
p3 = str(input("Mora perto da vítima?\n")).lower()
if p3 == "sim":
    pontos += 1
    print("Suspeito, próxima pergunta...")
elif p3 == "não":
    print("Certo, próxima pergunta...")
else:
    print("Resposta inválida!")
    exit(0)
p4 = str(input("Devia para a vítima?\n")).lower()
if p4 == "sim":
    pontos += 1
    print("Suspeito, próxima pergunta...")
elif p4 == "não":
    print("Certo, próxima pergunta...")
else:
    print("Resposta inválida!")
    exit(0)
p5 = str(input("Já trabalhou com a vítima?\n")).lower()
if p5 == "sim":
    pontos += 1
    print("Suspeito, próxima pergunta...")
elif p5 == "não":
    print("Certo, próxima pergunta...")
else:
    print("Resposta inválida!")
    exit(0)

if pontos == 2:
    print("Você é um SUSPEITO...")
elif pontos >= 3 and pontos <= 4:
    print("Você é um CÚMPLICE!")
elif pontos == 5:
    print("Você é o ASSASSINO!")
else:
    print("Você é INOCENTE, vaza!")

print("PONTUAÇÃO FINAL: " + str(pontos))