# Faça um programa que receba um número digitado pelo usuário e calcule a soma de
# todos os números de 1 até ao número digitado. Por exemplo, se o usuário digitou o
# número 4, a saída deve ser 10.

def soma_ate_numero(numero):
    #Calcula a soma dos números de 1 até o número informado.

    # Args:
    #     numero: O número até o qual a soma será calculada.

    # Returns:
    #     A soma dos números de 1 até o número informado.
    
    soma = 0
    for i in range(1, numero + 1):
        soma += i
    return soma

# Entrada do usuário
numero = int(input("Digite um número: "))

# Chamada da função e exibição do resultado
resultado = soma_ate_numero(numero)
print(f"A soma dos números de 1 até {numero} é: {resultado}")