preço = float(input("Digite o preço da mercadoria:"))
desconto = float(input("Digite o percentual de desconto:"))

valor_do_desconto = preço * desconto / 100
a_pagar = preço - valor_do_desconto

print("Um desconto de %5.2f %% em uma mercadoria de R$ %.2f" % (desconto, preço))
print("vale R$ %.2f." % valor_do_desconto)
print("O valor a pagar é de R$ %.2f" % a_pagar)