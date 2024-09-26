# Faça um programa para selecionar os elementos de uma lista, de forma a
# copiá-los para outras duas listas. Nesse caso, considere que, inicialmente,
# os valores estão na lista V = [9, 8, 7, 12, 0, 13 , 21], mas que devem ser
# copiados para a P, se forem pares; ou para I, se forem ímpares.


V = [9, 8, 7, 12, 0, 13, 21]
Pares = []
Impares = []

for numero in V:
  if numero % 2 == 0:
    Pares.append(numero)
  else:
    Impares.append(numero)

print("Números pares:", Pares)
print("Números ímpares:", Impares)