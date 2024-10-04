# Crie um programa que leia dois números e tente dividir o primeiro pelo
# segundo, tratando a exceção de divisão por zero.


def dividir_numeros():
  try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")
  except ZeroDivisionError:
    print("Não é possível dividir por zero!")

dividir_numeros()