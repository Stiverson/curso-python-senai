# ""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#         1. O produto do dobro do primeiro com metade do segundo .
#         2. A soma do triplo do primeiro com o terceiro.
#         3. O terceiro elevado ao cubo."""

int1 = input("Digite o primeiro inteiro: ")
int2 = input("Digite o segundo inteiro: ")
real = input("Digite um numer real: ")

produto = (int(int1) * 2) * (int(int2) / 2)

soma = (int(int1) * 3) + float(real)

potencia = float(real)**3

print("Produto do dobro do primeiro com metade do segundo: %d" % produto)
print("Soma do triplo do primeiro com o terceiro: %.2f" % soma)
print("Numero real elevado ao cubo: %.2f" % potencia)