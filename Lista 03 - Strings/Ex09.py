'''
Verificação de CPF: Leia um CPF no formato xxx.xxx.xxx-xx e valide os dígitos verificadores.
'''

cpf = str(input("Insira seu CPF no formato xxx.xxx.xxx-xx: \n"))
cpfSemPontos = cpf.replace(".", "")
cpfTratado = cpfSemPontos.replace("-", "")

if len(cpfTratado) == 11:
    if cpfTratado in ['00000000000', '11111111111', '22222222222', '33333333333', '44444444444', '55555555555', '66666666666', '77777777777', '88888888888', '99999999999']:
        print("Seu CPF NÃO é válido!")
    else:
        soma = 0
        for i in range(9):
            soma += int(cpfTratado[i]) * (10 - i)
        resto = soma % 11
        dig1 = 0 if resto < 2 else 11 - resto

        soma = 0
        for i in range(10):
            soma += int(cpfTratado[i]) * (11 - i)
        resto = soma % 11
        dig2 = 0 if resto < 2 else 11 - resto

        if dig1 == int(cpfTratado[9]) and dig2 == int(cpfTratado[10]):
            print("Seu CPF é válido!")
else:
    print("Seu CPF NÃO é válido!")