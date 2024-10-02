def calcular_salario_atual(salario_inicial=1000):
    #Calcula o salário atual de um funcionário com base nos aumentos anuais.

    # Args:
    #     salario_inicial (int, optional): Salário inicial do funcionário. Defaults to 1000.

    # Returns:
    #     float: Salário atual do funcionário.

    ano_inicial = 1995
    ano_atual = 2023  # Substitua pelo ano atual desejado

    percentual_aumento = 1.5  # Aumento de 1996
    salario_atual = salario_inicial

    for ano in range(ano_inicial + 1, ano_atual + 1):
        salario_atual *= (1 + percentual_aumento / 100)
        percentual_aumento *= 2

    return salario_atual

# Solicitar o salário inicial ao usuário (opcional)
salario_inicial_usuario = input("Digite o salário inicial (ou pressione Enter para usar o padrão R$1.000,00): ")
if salario_inicial_usuario:
    salario_inicial = float(salario_inicial_usuario)

# Calcular e exibir o salário atual
salario_final = calcular_salario_atual(salario_inicial)
print(f"O salário atual do funcionário é: R$ {salario_final:.2f}")