# Escreva um programa que leia uma entrada do usuário e converta para um
# número inteiro, tratando a exceção se a entrada não for um número.

def converter_para_inteiro():
  try:
    numero = int(input("Digite um número inteiro: "))
    print(f"O número convertido é: {numero}")
  except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")

converter_para_inteiro()