# O Hipermercado PagSempreMais está com uma promoção de carnes que é imperdível.
# Confira:
# Até 5 Kg Acima de 5 Kg
# Filé Duplo R$ 4,90 por Kg R$ 5,80 por Kg
# Alcatra R$ 5,90 por Kg R$ 6,80 por Kg
# Picanha R$ 6,90 por Kg R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de
# carne da promoção, porém não há limites para a quantidade de carne por cliente. Se
# compra for feita no cartão PagSempreMais o cliente receberá ainda um desconto de
# 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de
# carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da
# compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do
# desconto e valor a pagar.

def gerar_cupom_fiscal():
    """Gera um cupom fiscal para a promoção de carnes do Hipermercado PagSempreMais."""

    # Preços das carnes por faixa de peso
    precos = {
        "Filé Duplo": {"ate_5kg": 4.9, "acima_5kg": 5.8},
        "Alcatra": {"ate_5kg": 5.9, "acima_5kg": 6.8},
        "Picanha": {"ate_5kg": 6.9, "acima_5kg": 7.8}
    }

    # Solicitar informações ao cliente
    tipo_carne = input("Digite o tipo de carne (Filé Duplo, Alcatra ou Picanha): ").title()
    quantidade = float(input("Digite a quantidade de carne em kg: "))
    pagamento = input("Pagamento em cartão PagSempreMais? (sim/não): ").lower()

    # Calcular o preço total
    preco_por_kg = precos[tipo_carne]["acima_5kg" if quantidade > 5 else "ate_5kg"]
    preco_total = preco_por_kg * quantidade

    # Aplicar desconto
    desconto = 0
    if pagamento == "sim":
        desconto = preco_total * 0.05
        preco_total -= desconto

    # Imprimir o cupom fiscal
    print("\n--- Cupom Fiscal ---")
    print(f"Tipo de carne: {tipo_carne}")
    print(f"Quantidade: {quantidade:.2f} kg")
    print(f"Preço por kg: R$ {preco_por_kg:.2f}")
    print(f"Preço total: R$ {preco_total:.2f}")
    if desconto > 0:
        print(f"Desconto (5%): R$ {desconto:.2f}")
    print("-------------------")

# Chamar a função para gerar o cupom
gerar_cupom_fiscal()