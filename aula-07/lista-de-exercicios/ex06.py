# Faça um programa com uma função que necessite de uma argumento. A
# função retorna o valor do caractere ‘P’, se o seu argumento for positivo, e
# ‘N’, se o ser argumento for zero ou negativo.


def verifica_numero(numero):

  if numero > 0:
    return 'POSITIVO'
  else:
    return 'NEGATIVO'

numero = float(input("Digite um número: "))  # Permite números decimais

resultado = verifica_numero(numero)
print(f"O número {numero} é {resultado}.")