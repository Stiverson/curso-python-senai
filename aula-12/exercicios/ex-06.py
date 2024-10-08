# Escreva um programa que leia uma entrada do usuário e converta para um
# número decimal (float), tratando a exceção se a entrada não for um número.

def conversorDecimal(valor):
    
    try:
        return float(valor)
    except ValueError:
        print("O valor digitado não é um número válido.")
        return None
entrada = input("Digite um número decimal: ")

resultado = conversorDecimal(entrada)

if resultado is not None:
    print("O número digitado convertido é:", resultado)