# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do
# usuário. Calcule o total em segundos.


def converter_para_segundos(dias, horas, minutos, segundos):
  """Converte dias, horas, minutos e segundos para segundos.

  Args:
    dias: Quantidade de dias.
    horas: Quantidade de horas.
    minutos: Quantidade de minutos.
    segundos: Quantidade de segundos.

  Returns:
    O total de segundos.
  """

  # Convertendo cada unidade para segundos e somando
  total_segundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos
  return total_segundos

# Entrada de dados
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

# Chamando a função e imprimindo o resultado
resultado = converter_para_segundos(dias, horas, minutos, segundos)
print(f"O total em segundos é: {resultado}")