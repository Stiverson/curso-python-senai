# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o
# número do aluno e o segundo representando a sua altura em centímetros. Encontre o
# aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do
# aluno mais baixo, junto com suas alturas.

alunos = []

for i in range(10):
    numero_aluno = int(input("Digite o número do aluno: "))
    altura = float(input("Digite a altura do aluno em centímetros: "))
    alunos.append((numero_aluno, altura))

# Encontrar o aluno mais alto
mais_alto = max(alunos, key=lambda x: x[1])

# Encontrar o aluno mais baixo
mais_baixo = min(alunos, key=lambda x: x[1])

print(f"O aluno mais alto é o {mais_alto[0]} com {mais_alto[1]} cm.")
print(f"O aluno mais baixo é o {mais_baixo[0]} com {mais_baixo[1]} cm.")