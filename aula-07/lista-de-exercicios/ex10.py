# Escreva um programa, com uma função que leia 2 valores (A e B), calcule
# e mostre a soma dos números ímpares entre eles (inclusive A e B). Nesse
# caso, considere que só serão informados valores inteiros positivos e que A é
# menor que B.

def soma_impares(a, b):
  soma = 0
  for numero in range(a, b+1):
    if numero % 2 != 0:
      soma += numero
  return soma

a = int(input("Digite o primeiro número (A): "))
b = int(input("Digite o segundo número (B): "))

if a >= b:
  print("O primeiro número deve ser menor que o segundo.")
else:
 
  resultado = soma_impares(a, b)
  print(f"A soma dos números ímpares entre {a} e {b} é: {resultado}")