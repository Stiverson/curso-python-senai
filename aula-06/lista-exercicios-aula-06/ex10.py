preco = float(input("Digite o preço da mercadoria:"))
desconto = float(input("Digite o percentual de desconto:"))
valorDesconto = preco * desconto / 100
valorPagar = preco - valorDesconto

print("Seu desconto é de %5.2f %% em uma mercadoria de R$ %7.2f" % (desconto, preco))
print("O valor do desconto é R$ %7.2f." % valorDesconto)
print("O valor a pagar é de R$ %7.2f" % valorPagar)