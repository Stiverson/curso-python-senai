valor_compra = float(input("Digite o valor total da compra: R$ "))

if valor_compra <= 100:
    print("O pagamento deve ser feito em dinheiro.")
elif valor_compra <= 300:
    print("O pagamento pode ser feito no cartão de débito.")
else:
    print("O pagamento pode ser feito no cartão de crédito.")