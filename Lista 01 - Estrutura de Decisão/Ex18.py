'''
Faça um programa que peça uma data no formato dd/mm/aaaa e
determine se a mesma é uma data válida.
'''

# verificação do dia
dia = int(input("Insira o dia do mês: "))
if (dia <= 0) or (dia > 31):
    print("Dia inválido!")
    exit(0)
if len(str(dia)) > 2:
    print("Dia inválido!")
    exit(0)

# verificação do mês
mes = int(input("Insira o mês do ano: "))
if (mes <= 0) or (mes > 12):
    print("Mês inválido!")
    exit(0)
if len(str(mes)) > 2:
    print("Dia inválido!")
    exit(0)

# verificação do ano
ano = int(input("Insira o ano: "))
if ano <= 0:
    print("Ano inválido!")
    exit(0)
if (len(str(ano)) > 4) or (len(str(ano)) < 4):
    print("Ano inválido!")
    exit(0)
#cálculo ano bissexto
if ano % 4 == 0:
    if ano % 400 == 0:
        anoBissexto = True
    elif ano % 100 == 0:
        anoBissexto = False
    else:
        anoBissexto = True
else:
    anoBissexto = False
if (dia > 28) and (mes == 2) and (anoBissexto == False):
    print("Data inválida! Fevereiro só pode ter mais que 28 dias em um ano bissexto!")
    exit(0)

# mostrar a data validada
if (len(str(dia)) < 2) and (len(str(mes)) < 2):
    print("A data 0" + str(dia) + "/0" + str(mes) + "/" + str(ano) + " é válida!")
elif len(str(dia)) < 2:
    print("A data 0" + str(dia) + "/" + str(mes) + "/" + str(ano) + " é válida!")
elif len(str(mes)) < 2:
    print("A data " + str(dia) + "/0" + str(mes) + "/" + str(ano) + " é válida!")
else:
    print("A data " + str(dia) + "/" + str(mes) + "/" + str(ano) + " é válida!")