# Fazer um algoritmo que ao receber o salário atual de um funcionário, calcule o valor
# do novo salário reajustado de acordo com a tabela abaixo:
# Salário Atual Reajuste
# Abaixo de R$ 500,00 15%
# De R$ 500,00 até R$ 1000,00 10%
# Acima de R$ 1000,00 5%

def calcular_novo_salario(salario_atual):
  # Calcula o novo salário com base em uma tabela de reajuste.

  # Args:
  #   salario_atual: O salário atual do funcionário.

  # Returns:
  #   O novo salário reajustado.

  if salario_atual < 500:
    reajuste = 0.15
  elif salario_atual <= 1000:
    reajuste = 0.10
  else:
    reajuste = 0.05

  novo_salario = salario_atual + (salario_atual * reajuste)
  return novo_salario

# Entrada de dados
salario_atual = float(input("Digite o salário atual: "))

# Cálculo do novo salário
novo_salario = calcular_novo_salario(salario_atual)

# Impressão do resultado
print(f"O novo salário é: R$ {novo_salario:.2f}")