# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# a. Até 5 Kg Acima de 5 Kg
# b. Morango R$ 2,50 por Kg R$ 2,20 por Kg
# c. Maçã R$ 1,80 por Kg R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar
# R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um
# algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de
# maças adquiridas e escreva o valor a ser pago pelo cliente.

def calcular_preco_fruta(fruta, quantidade):
   
    preco_por_kg = {
        "morango": 2.5 if quantidade <= 5 else 2.2,
        "maçã": 1.8 if quantidade <= 5 else 1.5
    }
    return preco_por_kg[fruta] * quantidade

def aplicar_desconto(valor_total):
   
    if valor_total > 25:
        return valor_total * 0.9
    return valor_total


morangos = float(input("Digite a quantidade de morangos em kg: "))
macas = float(input("Digite a quantidade de maçãs em kg: "))


preco_morangos = calcular_preco_fruta("morango", morangos)
preco_macas = calcular_preco_fruta("maçã", macas)


valor_total = preco_morangos + preco_macas


valor_com_desconto = aplicar_desconto(valor_total)


print(f"O valor total a ser pago é: R$ {valor_com_desconto:.2f}")