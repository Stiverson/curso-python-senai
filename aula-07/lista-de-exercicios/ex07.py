# Faça um programa com uma função chamada somaImposto. A função
# possui dois parâmetros formais: taxaImposto, que é a quantia de imposto
# sobre vendas expressa em porcentagem e, custo, que é o custo de um item
# antes do imposto. A função “altera” o valor de custo para incluir o imposto
# sobre vendas.

def soma_imposto(custo, taxa_imposto):
  
  taxa_decimal = taxa_imposto / 100
  valor_imposto = custo * taxa_decimal
  valor_total = custo + valor_imposto

  return valor_total

custo_produto = float(input("Digite o valor do produto: "))
taxa_imposto = float(input("Digite a taxa de imposto (%): "))

valor_final = soma_imposto(custo_produto, taxa_imposto)

print(f"O valor total do produto com o imposto é: R$ {valor_final:.2f}")