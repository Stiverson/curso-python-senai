num = int(input('Digite um numero para ver a sua tabuada: '))

for calc in range(0,11):
    print('{} X {} = {}'.format(num ,calc,(num * calc)))