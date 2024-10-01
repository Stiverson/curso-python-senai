# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# Até 5 Kg Acima de 5 Kg
# Morango R$ 2,50 por Kg R$ 2,20 por Kg
# Maçã R$ 1,80 por Kg R$ 1,50 por Kg

# Lista de Revisão

# Estruturas – Sequencial, Decisão, Repetição, Listas, Funções
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$
# 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo
# para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
# adquiridas e escreva o valor a ser pago pelo cliente.

def calcular_preco_fruta(fruta, quantidade):
    # """Calcula o preço de uma fruta de acordo com a quantidade."""
    preco_por_kg = {
        "morango": 2.5 if quantidade <= 5 else 2.2,
        "maçã": 1.8 if quantidade <= 5 else 1.5
    }
    return preco_por_kg[fruta] * quantidade

def aplicar_desconto(valor_total):
    # """Aplica um desconto de 10% se o valor total for maior que R$25."""
    if valor_total > 25:
        return valor_total * 0.9
    return valor_total

# Entrada de dados
morangos = float(input("Digite a quantidade de morangos em kg: "))
macas = float(input("Digite a quantidade de maçãs em kg: "))

# Cálculo dos preços
preco_morangos = calcular_preco_fruta("morango", morangos)
preco_macas = calcular_preco_fruta("maçã", macas)

# Cálculo do valor total
valor_total = preco_morangos + preco_macas

# Aplicação do desconto
valor_com_desconto = aplicar_desconto(valor_total)

# Saída
print(f"O valor total a ser pago é: R$ {valor_com_desconto:.2f}")