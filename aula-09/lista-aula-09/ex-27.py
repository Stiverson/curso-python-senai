# Faça um programa que converta uma lista de temperaturas de Fahrenheit para Celsius,
# em seu programa o usuário deverá inserir uma sequência de valores que representam
# a temperatura em graus Fahrenheit, seu programa deve receber esses valores e
# armazenar em uma lista até que o valor inserido pelo usuário seja um valor em branco
# (uma string vazia). Converta todos os valores presentar na lista para graus Celsius e
# imprima na tela em uma formatação amigável ao usuário.
# Exemplos de entrada Exemplos de saída
# 86 86 ºF corresponde a 30 ºC
# 77 77 ºF corresponde a 25 ºC
# 89.6 89.6 ºF corresponde a 32 ºC
# 73.4 73.4 ºF corresponde a 23 ºC
# 69.8 69.8 ºF corresponde a 21 ºC

def fahrenheit_para_celsius(fahrenheit):
#  Converte uma temperatura de Fahrenheit para Celsius.

  celsius = (fahrenheit - 32) * 5/9
  return celsius

def main():
  temperaturas_fahrenheit = []
  temperatura = input("Digite uma temperatura em Fahrenheit (ou pressione Enter para finalizar): ")

  while temperatura:
    temperaturas_fahrenheit.append(float(temperatura))
    temperatura = input("Digite uma temperatura em Fahrenheit (ou pressione Enter para finalizar): ")

  for temperatura_fahrenheit in temperaturas_fahrenheit:
    temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)
    print(f"{temperatura_fahrenheit:.1f} ºF corresponde a {temperatura_celsius:.1f} ºC")

if __name__ == "__main__":
  main()