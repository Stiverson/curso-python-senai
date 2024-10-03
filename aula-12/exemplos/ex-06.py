try:
    dividendo = int(input("Digite o dividendo: "))
    divisor = int(input("Digite o divisor: "))
    resultado = dividendo / divisor

except(ZeroDivisionError, ValueError):
    print("Erro de conversão ou divisor igual a zero")