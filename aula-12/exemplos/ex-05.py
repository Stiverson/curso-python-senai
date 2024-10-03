try:
    dividendo = int(input("Digite o dividendo: "))
    divisor = int(input("Digite o divisor: "))
    resultado = dividendo / divisor

except ValueError:
    print("Número digitado inválido!")

except ZeroDivisionError:
    print("Divisão por Zero não permitida!")