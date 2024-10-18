# Faça um Programa que leia dois vetores (lista) com 10 elementos cada. Gere um
# terceiro vetor de 20 elementos vindos dos dois vetores anteriores.

primeiraLista = []
segundaLista = []

while True:
    e = int(input("Digite 10 valores para a primeira lista (0 para finalizar a lista): "))
    if e == 0:
        break
    primeiraLista.append(e)
while True:
    e = int(input("Digite 10 valores11 para a segunda lista (0 para finalizar a lista): "))
    if e == 0:
        break
    segundaLista.append(e)

terceiraLista = primeiraLista[:]  
terceiraLista.extend(segundaLista)
x = 0
while x < len(terceiraLista):
    print(f"{x}: {terceiraLista[x]}")
    x = x + 1