def concatenar_tipos():
  try:
    texto = (input("Digite um texto qualquer : "))
    numero = int(input("Digite um numero qualquer: "))
    resultado = texto + numero
    print(resultado)
  except TypeError:
    print("Não é possível concatenar tipos diferentes.")

concatenar_tipos()