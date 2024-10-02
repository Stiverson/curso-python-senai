# Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:


def calcular_area_trapezio(base_maior, base_menor, altura):
#  Calcula a área de um trapézio.

#   Args:
#     base_maior: A medida da base maior do trapézio.
#     base_menor: A medida da base menor do trapézio.
#     altura: A altura do trapézio.

#   Returns:
#     A área do trapézio.

  area = ((base_maior + base_menor) * altura) / 2
  return area

# Solicita ao usuário que insira os valores
base_maior = float(input("Digite o valor da base maior: "))
base_menor = float(input("Digite o valor da base menor: "))
altura = float(input("Digite o valor da altura: "))

# Chama a função para calcular a área
area = calcular_area_trapezio(base_maior, base_menor, altura)

# Imprime o resultado
print("A área do trapézio é:", area)