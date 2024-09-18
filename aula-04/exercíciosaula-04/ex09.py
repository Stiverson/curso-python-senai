import math

numero = float(input("Digite um número: "))

if numero >= 0:
    raiz_quadrada = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}")
else:
    quadrado = numero ** 2
    print(f"O quadrado de {numero} é {quadrado}")