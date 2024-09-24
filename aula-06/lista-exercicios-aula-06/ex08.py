num1 = float(input("Digite o primerio número: \n"))
num2 = float(input("Digite o segundo numero número : \n"))
menu = (
'''\nMENU DE OPERAÇÕES:
[1] soma
[2] subtração
[3] divisão
[4] multiplicação
[5] NUMERO maior ou menor
[6] encerrar o programa\n '''
)
maior = 0
menor = 0

print(menu)

user = int(input("Sua escolha (opções de 1 a 6): \n"))
while user != 6:
    if user > 5: 
        print("Warning: escolha um número de 1 a 5.")
        user = int(input("Sua escolha: \n"))
    elif user < 0:  
        print("Warning: escolha um número positivo.")
        user = int(input("Sua escolha: \n"))
    else: 
        if user == 1: 
            print("Vocẽ escolheu soma!")
            print("Resultado da soma: \n{} + {} = {}".format(num1, num2, (num1 + num2)))
            print(menu)
            user = int(input("Sua escolha: \n"))
        elif user == 2:  
            print("Você escolheu subtração!")
            print("Resultado da subtração: \n{} - {} = {:.0f}".format(num1, num2, (num1 - num2)))
            print(menu)
            user = int(input("Sua escolha: \n"))
        elif user == 3:  
            print("Você escolheu divisão!")
            print("Resultado da divisão: \n{} - {} = {:.0f}".format(num1, num2, (num1 / num2)))
            print(menu)
            user = int(input("Sua escolha: \n"))
        elif user == 4: 
            print("Você escolheu multiplicação!")
            print("Resultado da multiplicação: \n{} x {} = {:.0f}".format(num1, num2, (num1 * num2)))
            print(menu)
            user = int(input("Sua escolha: \n"))
        elif user == 5: 
            if num1 > num2:
                maior = num1
                menor = num2
                print("O maior é {} e o menor é {}.".format(maior, menor))
                print(menu)
            elif num2 > num1:
                maior = num2
                menor = num1
                print("O maior é {} e o menor é {}.".format(maior, menor))
                print(menu)
            else:
                print("Os dois números são idênticos.")
                print(menu)
            user = int(input("Sua escolha: \n")) 
print("Opção 6: programa encerrado.")