# Faça um programa com uma função que retorne o maior de dois números.

def verificar(num_1,num_2):
    if num_1 >= num_2:
        print("O primeiro numero digitado {} é maior:".format(num_1))
    else:
        print("O Segundo  digitado {} é maior:".format(num_2))
        
num_1 = int(input("Digite um numero : "))
num_2 = int(input("Digite outro numero : "))

verificar(num_1,num_2)