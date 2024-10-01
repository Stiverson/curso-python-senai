# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
# descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela
# abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas
# não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao
# Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua
# hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# a. Salário Bruto até 900 (inclusive) - isento
# b. Salário Bruto até 1500 (inclusive) - desconto de 5%
# c. Salário Bruto até 2500 (inclusive) - desconto de 10%
# d. Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as
# informações, dispostas conforme o exemplo abaixo. No exemplo o valor da
# hora é 5 e a quantidade de hora é 220.
# e. Dar a saída formatada como abaixo:
# Salário Bruto: (5 * 220) : R$ 1100,00
# (-) IR (5%) : R$ 55,00
# (-) INSS (10%) : R$ 110,00
# FGTS (11%) : R$ 121,00
# Total de Descontos : R$ 165,00
# Salário Líquido : R$ 935,00

def calcular_folha_pagamento(valor_hora, horas_trabalhadas):
    # """Calcula a folha de pagamento com base nos dados fornecidos."""

    # Cálculo do salário bruto
    salario_bruto = valor_hora * horas_trabalhadas

    # Cálculo do desconto do IR
    if salario_bruto <= 900:
        desconto_ir = 0
    elif salario_bruto <= 1500:
        desconto_ir = salario_bruto * 0.05
    elif salario_bruto <= 2500:
        desconto_ir = salario_bruto * 0.1
    else:
        desconto_ir = salario_bruto * 0.2

    # Cálculo do desconto do sindicato
    desconto_sindicato = salario_bruto * 0.03

    # Cálculo do FGTS
    fgts = salario_bruto * 0.11

    # Cálculo do salário líquido
    salario_liquido = salario_bruto - (desconto_ir + desconto_sindicato)

    # Impressão formatada dos resultados
    print(f"Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"(-) IR ({desconto_ir/salario_bruto*100:.0f}%): R$ {desconto_ir:.2f}")
    print(f"(-) Sindicato (3%): R$ {desconto_sindicato:.2f}")
    print(f"FGTS (11%): R$ {fgts:.2f}")
    print(f"Total de Descontos: R$ {desconto_ir + desconto_sindicato:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

# Entrada de dados pelo usuário
valor_hora = float(input("Digite o valor da hora trabalhada: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

# Chamada da função para calcular a folha de pagamento
calcular_folha_pagamento(valor_hora, horas_trabalhadas)