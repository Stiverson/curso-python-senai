n1 = int(input('Digite um numero : '))

fatorial = 1
for calculo in range(n1, 0, -1):
    print(calculo, end='')
    print(' x 'if calculo > 1 else ' = ',end='')
    fatorial = fatorial * calculo

print(fatorial)