# Faça um programa que percorra duas listas e gere uma terceira com
# elementos das duas primeiras.


primeiraLista = []
segundaLista = []

while True:
    e = int(input("Digite um valor para a primeira lista (0 para finalizar a lista): "))
    if e == 0:
        break
    primeiraLista.append(e)
while True:
    e = int(input("Digite um valor para a segunda lista (0 para finalizar a lista): "))
    if e == 0:
        break
    segundaLista.append(e)

terceiraLista = primeiraLista[:]  
terceiraLista.extend(segundaLista)
x = 0
while x < len(terceiraLista):
    print(f"{x}: {terceiraLista[x]}")
    x = x + 1