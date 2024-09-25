# Faça um programa com uma função que receba o raio (R) de um círculo e
# retorne a sua área. Fórmula: A = pi * R2.

num_1 = float(input("Digite o valor do raio do circulo : "))

def area_circulo(num_1):
    return 3,14 * num_1**2

print("A área do raio do circulo digitado é {} ".format(area_circulo(num_1)))

area_circulo(num_1)