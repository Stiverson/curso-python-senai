# Faça um programa que leia 4 notas, armazene em um vetor e mostre as
# notas e a média na tela.

notas = [0,0,0,0]

soma = 0
x =0

while x < 4:
    notas[x] = float(input("Nota %d: " % x ))
    soma += notas[x]
    x += 1
x = 0
while x < 4:
    print("Nota %d: %6.2f" % (x, notas[x]))
    x += 1

media   = soma / x
print("Media: %5.2f" % media)