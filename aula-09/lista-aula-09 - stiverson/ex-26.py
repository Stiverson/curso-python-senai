import math

def calcular_raizes(a, b, c):
#   Calcula as raízes de uma equação de segundo grau.
  if a == 0:
    print("Não é uma equação de segundo grau.")
    return None

  delta = b**2 - 4*a*c

  if delta < 0:
    print("Não existem raízes reais.")
    return None
  elif delta == 0:
    x = -b / (2*a)
    print("Raiz única:", x)
    return (x,)
  else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Duas raízes reais:", x1, x2)
    return (x1, x2)

# Exemplo de uso:
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

raizes = calcular_raizes(a, b, c)