primeiroValor = int(input('Digite o primeiro  valor: '))
segundoValor = int(input('Digite o segundo valor: '))


if segundoValor == 0:
    print('O valor inserido não pode ser zero')
else:
    divisao = primeiroValor / segundoValor
    print('A soma dos dois valores é : ',divisao)