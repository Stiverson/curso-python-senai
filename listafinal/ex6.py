# A série de Fibonacci é formada pela sequência 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... .
# Faça um programa que gere a série até que o valor seja maior que 500.

def fibo_int(limit):
    a, b = 0, 1
    while a <= limit:
        user_input = input(f"Valor atual: {a}. Deseja Continuar? (s/n): ")
        if user_input.lower() == 'n':
            break
        print(a)
        a, b = b, a + b


fibo_int(500)