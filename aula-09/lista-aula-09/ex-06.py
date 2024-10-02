# Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar
# se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se
# o mesmo é: equilátero, isósceles ou escaleno. Dicas:
# - Três lados formam um triângulo quando a soma de quaisquer dois lados for maior
# que o terceiro;
# - Triângulo equilátero – três lados iguais
# - Triângulo isósceles – quaisquer dois lados iguais
# - Triângulo escaleno – três lados diferentes

def classificar_triangulo(lado1, lado2, lado3):
  # Classifica um triângulo de acordo com os seus lados.

  # Verifica se os lados formam um triângulo
  if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    # É um triângulo
    if lado1 == lado2 == lado3:
      return "Os valores do triângulo digitado é um triângulo Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
      return "Os valores do triângulo digitado é um triângulo Isósceles"
    else:
      return "Os valores do triângulo digitado é um triângulo Escaleno"
  else:
    return "Não é um triângulo"

# Entrada de dados
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

# Classificação do triângulo
resultado = classificar_triangulo(lado1, lado2, lado3)

# Impressão do resultado
print(resultado)