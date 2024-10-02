# O cardápio de uma lanchonete é o seguinte:
# Especificação Código Preço
# Cachorro Quente 100 R$ 1,20
# Bauru Simples 101 R$ 1,30
# Bauru com ovo 102 R$ 1,50
# Hambúrguer 103 R$ 1,20
# Cheeseburguer 104 R$ 1,30
# Refrigerante 105 R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do
# pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.


def calcular_pedido():
    cardapio = {100: 1.20, 101: 1.30, 102: 1.50, 103: 1.20, 104: 1.30, 105: 1.00}
    total_geral = 0

    while True:
        codigo = int(input("Digite o código do item (0 para finalizar): "))
        if codigo == 0:
            break

        quantidade = int(input("Digite a quantidade: "))

        if codigo in cardapio:
            valor_item = cardapio[codigo] * quantidade
            total_geral += valor_item
            print(f"Item {codigo}: R$ {valor_item:.2f}")
        else:
            print("Código inválido.")

    print(f"Total do pedido: R$ {total_geral:.2f}")

calcular_pedido()