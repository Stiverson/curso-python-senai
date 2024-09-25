# Faça um programa que leia um vetor de 10 números inteiros e mostre-os na
# tela na ordem inversa.

numeros = []

for i in range(10):
    numeros.append(float(input(f"Digite o {i+1}º numero real: ")))


print("Os numeros inversos são: ", end="")

for numero in numeros[::-1]:
    print(f" {numero}", end="")