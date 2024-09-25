# Faça um programa com uma função que receba dois números e retorne True
# se o primeiro for múltiplo do segundo.

num_1 = int(input("Digite um numero : "))
num_2 = int(input("Digite outro numero : "))

def multiplo(a, b):
    return a % b == 0
if num_1 == True:
    print("O primeiro numero digitado {} é multiplo do {}:".format(num_1,num_2))
else:
    print("O Segundo  numero digitado {} é multiplo do {}:".format(num_2,num_1))
        
multiplo(num_1,num_2)