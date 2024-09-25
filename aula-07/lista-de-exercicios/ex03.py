# Faça um programa com uma função que receba o lado (l) de um quadrado e
# retorne a sua área (A = lado2).

num_1 = int(input("Digite o valor do lado do quadarado : "))

def area_quadrado(num_1):
    return num_1**2

print("A área do quadrado digitado é {} ".format(area_quadrado(num_1)))

area_quadrado(num_1)