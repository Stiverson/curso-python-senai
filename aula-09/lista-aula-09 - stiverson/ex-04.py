# O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10
# caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu uma
# tabela que contém o número de itens que o cliente comprou e ao lado o valor da
# conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente
# está levando e olhar na tabela de preços. Você foi contratado para desenvolver o
# programa que monta esta tabela de preços, que conterá os preços de 1 até 50
# produtos, conforme o exemplo abaixo:
# Lojas Quase Dois - Tabela de preços
# 1 - R$ 1.99
# 2 - R$ 3.98
# ...
# 50 - R$ 99.50

def gerar_tabela_precos(quantidade_maxima):
  # Gera uma tabela de preços para uma loja de R$ 1,99.

  valor_unitario = 1.99
  tabela = []
  for quantidade in range(1, quantidade_maxima + 1):
      valor_total = quantidade * valor_unitario
      tabela.append(f"Valor por quantidade {quantidade} - R$ {valor_total:.2f}")

  return "\n".join(tabela)

# Definir a quantidade máxima de produtos
quantidade_maxima = 50

# Gerar e imprimir a tabela
tabela_precos = gerar_tabela_precos(quantidade_maxima)
print("-----------------------------------")
print("Lojas Quase Dois - Tabela de preços")
print("-----------------------------------")
print(tabela_precos)
print("-----------------------------------")