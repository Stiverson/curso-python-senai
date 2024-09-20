numPar = 0
numImpar = 0

numero = int(input("Digite um numero ou digite 0 para parar: "))

while numero != 0:
    if numero % 2 == 1:
        numImpar +=1
    else:
        numPar +=1
    numero = int(input("Digite um numero ou digite 0 para parar: "))

print("Numero impares contam: ", numImpar)
print("Numero pares contam: ", numPar)

