# Faça um programa que calcule as raízes de uma equação do segundo grau, na
# forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as
# consistências, informando ao usuário nas seguintes situações:
# a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo
# grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# b. Se o delta calculado for negativo, a equação não possui raízes reais. Informe
# ao usuário e encerre o programa;
# c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
# informe-a ao usuário;
# d. Se o delta for positivo, a equação possui duas raízes reais; informe-as ao
# usuário.

import math

def calculoDeRaizes(a, b, c):

  if a == 0:
    print("Esta não é uma equação de segundo grau.")
    return None

  delta = b**2 - 4*a*c

  if delta < 0:
    print("Não existem raízes reais.")
    return None
  elif delta == 0:
    x = -b / (2*a)
    print("O resultado é uma Raiz única:", x)
    return (x,)
  else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Duas raízes reais:", x1, x2)
    return (x1, x2)


a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

raizes = calculoDeRaizes(a, b, c)