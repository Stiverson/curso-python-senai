# Crie um programa que leia dois números e tente dividir o primeiro pelo segundo, tratando a exceção de divisão por zero e de valor inválido.

def divizaoValores():

    try:
        
        numerador = float(input("Digite o numerador: "))
        denominador = float(input("Digite o denominador: "))

        resultado = numerador / denominador

        print(f"O resultado da divisão é: {resultado}")

    except ZeroDivisionError:
        print("Não é possível dividir por zero.")
    except ValueError:
        print("Digite apenas números válidos.")
    except Exception as e: 
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    divizaoValores()


