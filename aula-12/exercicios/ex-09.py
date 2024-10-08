# Crie um programa que leia um número e calcule sua raiz quadrada, tratando a exceção se o número for negativo.

import math

def calculoRaiz():
    while True:
        try:
            numero = float(input("Digite um número: "))
            if numero < 0:
                raise ValueError("O número deve ser positivo.")
            raiz = math.sqrt(numero)
            print(f"A raiz quadrada de {numero} é {raiz:.2f}")
            break
        except ValueError as e:
            print(f"Erro: {e}")

calculoRaiz()