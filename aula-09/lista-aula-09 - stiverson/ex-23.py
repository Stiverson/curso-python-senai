# Escreva um programa que pergunte a quantidade de km percorridos por um carro
# alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km
# rodado.

def calcular_aluguel():
# Calcula o valor total do aluguel de um carro, considerando o número de dias e quilômetros rodado

  dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))
  km = float(input("Digite a quantidade de quilômetros percorridos: "))

  valor_por_dia = 60.0
  valor_por_km = 0.15

  valor_dias = dias * valor_por_dia
  valor_km = km * valor_por_km
  valor_total = valor_dias + valor_km

  print(f"O valor total a pagar pelo aluguel é de R$ {valor_total:.2f}")

calcular_aluguel()