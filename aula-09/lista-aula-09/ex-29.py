# Escreva o menu de opções abaixo. Leia a opção ao do usuário e execute a operação
# escolhida. Escreva uma mensagem de erro se a opção for inválida.
# Escolha a opção:
# 1- Soma de 2 números.
# 2- Diferença entre 2 números (maior pelo menor).
# 3- Produto entre 2 números.
# 4- Divisão entre 2 números (o denominador não pode ser zero).
# Opção:

def soma(num1, num2):
    return num1 + num2

def diferenca(num1, num2):
    return abs(num1 - num2)

def produto(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Divisão por zero não é permitida."
    else:
        return num1 / num2

while True:
    print("Escolha a opção:")
    print("1- Soma de 2 números.")
    print("2- Diferença entre 2 números (maior pelo menor).")
    print("3- Produto entre 2 números.")
    print("4- Divisão entre 2 números (o denominador não pode ser zero).")
    print("5- Sair")

    opcao = input("Opção: ")

    if opcao == '1':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = soma(num1, num2)
        print("Resultado da soma:", resultado)
    elif opcao == '2':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = diferenca(num1, num2)
        print("Resultado da diferença:", resultado)
    elif opcao == '3':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = produto(num1, num2)
        print("Resultado do produto:", resultado)
    elif opcao == '4':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = divisao(num1, num2)
        print("Resultado da divisão:", resultado)
    elif opcao == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")