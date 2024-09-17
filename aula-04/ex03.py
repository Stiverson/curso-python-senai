primeiroValor = int(input('Digite o primeiro  valor: '))
segundoValor = int(input('Digite o segundo valor: '))

divisao = primeiroValor / segundoValor

if segundoValor == 0:
    print('O valor inserido não pode ser zero')
else:
    print('A soma dos dois valores é : ',divisao)