valorProduto = float(input('Digite o valor do produto: '))

desconto = valorProduto * 0.10
valorComDesconto = valorProduto - desconto

print('Valor do produto com desconto é : R$ %.2f' %valorComDesconto)