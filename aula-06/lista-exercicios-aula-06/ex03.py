while True:
    primeiroNumero = float(input("Primeiro número: "))
    segundoNumero = float(input("Segundo número: "))
    operação = input("Digite a operação a realizar (+, -, * ou /) ou 'sair' para encerrar: ")

    if operação == "sair":
        print("Encerrando o programa.")
        break
    elif operação == "+":
        resultado = primeiroNumero + segundoNumero
    elif operação == "-":
        resultado = primeiroNumero - segundoNumero
    elif operação == "*":
        resultado = primeiroNumero * segundoNumero
    elif operação == "/":
        resultado = primeiroNumero / segundoNumero
    else:
        print("Operação inválida!")
        resultado = 0

    print("Resultado: ", resultado)
