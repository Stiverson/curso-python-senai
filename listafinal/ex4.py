# Faça um programa que leia e valide as seguintes informações:
# a. Nome: maior que 3 caracteres;
# b. Idade: entre 0 e 150;
# c. Salário: maior que zero;
# d. Sexo: 'f' ou 'm';
# e. Estado Civil: 's', 'c', 'v', 'd'

def validar_informacoes():
    while True:
        nome = input("Digite seu nome (maior que 3 caracteres): ")
        if len(nome) > 3:
            break
        else:
            print("Nome inválido. Digite um nome com mais de 3 caracteres.")

    while True:
        idade = int(input("Digite sua idade (entre 0 e 150): "))
        if 0 <= idade <= 150:
            break
        else:
            print("Idade inválida. Digite uma idade entre 0 e 150.")

    while True:
        salario = float(input("Digite seu salário (maior que zero): "))
        if salario > 0:
            break
        else:
            print("Salário inválido. Digite um salário maior que zero.")

    while True:
        sexo = input("Digite seu sexo (f/m): ").lower()
        if sexo in ('f', 'm'):
            break
        else:
            print("Sexo inválido. Digite 'f' ou 'm'.")

    while True:
        estado_civil = input("Digite seu estado civil (s/c/v/d): ").lower()
        if estado_civil in ('s', 'c', 'v', 'd'):
            break
        else:
            print("Estado civil inválido. Digite 's', 'c', 'v' ou 'd'.")

    print("\nInformações Validadas:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: {salario}")
    print(f"Sexo: {sexo}")
    print(f"Estado Civil: {estado_civil}")

validar_informacoes()