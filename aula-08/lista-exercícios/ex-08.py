# Faça um programa peça a idade e a altura de 5 pessoas, armazene cada
# informação no seu respectivo vetor. Imprima a idade e a altura na ordem
# inversa à ordem lida.


idades = []
alturas = []

# Pedindo as informações para 5 pessoas
for i in range(5):
    idade = int(input("Digite a idade da pessoa {}: ".format(i+1)))
    altura = float(input("Digite a altura da pessoa {}: ".format(i+1)))
    idades.append(idade)
    alturas.append(altura)

# Invertendo as listas
idades.reverse()
alturas.reverse()

# Imprimindo as informações na ordem inversa
for i in range(5):
    print("Pessoa {}: Idade = {}, Altura = {}".format(i+1, idades[i], alturas[i]))