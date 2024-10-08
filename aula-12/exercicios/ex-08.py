# Escreva uma função que recebe dois argumentos e retorna sua soma. Trate a exceção caso os argumentos não sejam números.

def somaDosValores():
   
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            resultado = num1 + num2
            print(f"A soma mágica de {num1} e {num2} é... {resultado}! Shazam caramba!")

        except ValueError:
            print("Ops! Parece que você tentou somar bananas com maçãs. Tente só números, ok?")
        except Exception as e:
            print(f"Algo deu errado! O mago da matemática está confuso: {e}")

        continuar = input("Deseja realizar outra soma? (sim/não): ")
        if continuar.lower() != "sim":
            break

if __name__ == "__main__":
    somaDosValores()