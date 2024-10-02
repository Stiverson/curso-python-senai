# Com a ajuda do fluxograma, crie um programa em Python que calcula o custo total e o
# troco, de itens comprados.


def calcular_compra():
# Calcula o custo total de uma compra e o troco.

  preco_por_unidade = float(input("Digite o preço por unidade: "))
  quantidade = int(input("Digite a quantidade de itens: "))
  valor_pago = float(input("Digite o valor pago: "))

  custo_total = preco_por_unidade * quantidade
  troco = valor_pago - custo_total

  print(f"Quantidade de itens: {quantidade}")
  print(f"Custo total: R$ {custo_total:.2f}")
  print(f"Troco: R$ {troco:.2f}")

# Chamando a função para executar o cálculo
calcular_compra()