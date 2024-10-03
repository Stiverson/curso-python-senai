def calcular_quadrado():
  try:
    numero = int(input("Digite um número inteiro: "))
    quadrado = numero ** 2
    print(f"O quadrado de {numero} é {quadrado}.")
  except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")

calcular_quadrado()