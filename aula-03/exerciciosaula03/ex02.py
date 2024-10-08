# Escreva um programa que leia um valor em metros e o exiba convertido em
# milímetros. Para converter em milímetros, use a tabela:

# Km -> x 10 - hm -> x 10 - dam -> x 10 - m -> x 10 - dm 
# m -> x 10



valor_m = int(input("Digite um valor em metros: "))
valor_mm = valor_m * 1000 
print(f"Valor em milimetros: {valor_mm } mm")