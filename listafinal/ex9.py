# Faça um Programa que leia um número inteiro menor que 1000 e imprima a
# quantidade de centenas, dezenas e unidades dele.
# a. Observando os termos no plural a colocação do "e", da vírgula entre
# outros. Exemplo:
# b. 326 = 3 centenas, 2 dezenas e 6 unidades
# c. 12 = 1 dezena e 2 unidades
# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11,
# 1, 7 e 16

def unidades_dezenas_centenas(numero):
    
    if numero < 0 or numero >= 1000:
        print("O número digitado  não serve! Digite um número entre 0 e 999!")
        return

    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    mensagem = ""
    if centenas > 0:
        mensagem += f"{centenas} centena{'s' if centenas > 1 else ''} "
    if dezenas > 0:
        mensagem += f"{dezenas} dezena{'s' if dezenas > 1 else ''} "
    if unidades > 0:
        mensagem += f"e {unidades} unidade{'s' if unidades > 1 else ''} "
    elif centenas == 0 and dezenas == 0:
        mensagem = "Zero! Sem nada por aqui!"

    print(f"O número {numero} é composto por: {mensagem}")

numeros = [326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]
for numero in numeros:
    unidades_dezenas_centenas(numero)