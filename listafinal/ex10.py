# O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a
# metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi
# contratado para desenvolver o programa que monta a tabela de preços de pães, de
# 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo
# abaixo:
# Preço do pão: R$ 0.18
# Panificadora Pão de Ontem - Tabela de preços
# 1 - R$ 0.18
# 2 - R$ 0.36
# ...
# 50 - R$ 9.00

def gerar_tabela_precos(quantidade_maxima):
 

  valor_unitario = 1.99
  tabela = []
  for quantidade in range(1, quantidade_maxima + 1):
      valor_total = quantidade * valor_unitario
      tabela.append(f"Valor por quantidade {quantidade} - R$ {valor_total:.2f}")

  return "\n".join(tabela)


quantidade_maxima = 50


tabela_precos = gerar_tabela_precos(quantidade_maxima)
print("-----------------------------------")
print("Lojas Quase Dois - Tabela de preços")
print("-----------------------------------")
print(tabela_precos)
print("-----------------------------------")