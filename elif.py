opcao = int(input("informe uma opção: \n[1] sacar \n[2] extrato \n:"))

if opcao == 1:
    valor = float(input("informe uma quantia para o saque: "))

elif opcao == 2:
    print("exibindo extrato...")

else:
    print("opção inválida")
    SystemExit