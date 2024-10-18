# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e
# mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9)

def celsius_para_fahrenheit(celsius):


  fahrenheit = celsius * (9/5) + 32
  return fahrenheit

def fahrenheit_para_celsius(fahrenheit):

  celsius = (fahrenheit - 32) * 5/9
  return celsius

def main():
  while True:
    print("Menu de Conversão de Temperaturas:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
      celsius = float(input("Digite a temperatura em Celsius: "))
      fahrenheit = celsius_para_fahrenheit(celsius)
      print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")
    elif opcao == '2':
      fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
      celsius = fahrenheit_para_celsius(fahrenheit)
      print(f"{fahrenheit}°F equivale a {celsius:.2f}°C")
    elif opcao == '3':
      print("Saindo...")
      break
    else:
      print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
  main()