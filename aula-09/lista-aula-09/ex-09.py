# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
# (codificado da seguinte forma: A - álcool, G - gasolina), calcule e imprima o valor a ser
# pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro
# do álcool é R$ 1,90.

def calcular_valor_a_pagar(litros, tipo_combustivel):
    # Calcula o valor a ser pago por um abastecimento.

    preco_alcool = 1.90
    preco_gasolina = 2.50

    if tipo_combustivel.upper() == 'A':
        if litros <= 20:
            desconto = 0.03
        else:
            desconto = 0.05
        valor_total = litros * preco_alcool * (1 - desconto)
    elif tipo_combustivel.upper() == 'G':
        if litros <= 20:
            desconto = 0.04
        else:
            desconto = 0.06
        valor_total = litros * preco_gasolina * (1 - desconto)
    else:
        print("Tipo de combustível inválido.")
        return

    return valor_total

# Entrada de dados
litros = float(input("Digite a quantidade de litros abastecidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A - álcool, G - gasolina): ")

# Cálculo e impressão do valor a pagar
valor_a_pagar = calcular_valor_a_pagar(litros, tipo_combustivel)
if valor_a_pagar:
    print(f"O valor a ser pago é: R$ {valor_a_pagar:.2f}")