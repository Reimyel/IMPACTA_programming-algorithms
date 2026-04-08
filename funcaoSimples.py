def eh_par(numero):
    return numero % 2 == 0

def eh_impar(numero):
    return numero % 2 != 0

def interagir_com_usuario():
    print("---PAR-OU-IMPAR---")

    while True:
        try:
            entrada = input("Digite um número inteiro (ou 'sair' para terminar): ")

            if entrada.lower() == 'sair':
                print("VAZA")
                break
            
            numero = int(entrada)

            if eh_par(numero):
                print(f"Teu número {numero} é par")
                resultado_par = eh_par(numero)
                print(f"A função eh_par({numero}) retornou {resultado_par}")

            if eh_impar(numero):
                print(f"Teu número {numero} é impar")
                resultado_impar = eh_impar(numero)
                print(f"A função eh_impar({numero}) retornou {resultado_impar}")

        except ValueError:
            print("va tomanocu")
        except Exception as e:
            print(f"fodase tbm: {e}")

if __name__ == "__main__":
    interagir_com_usuario()