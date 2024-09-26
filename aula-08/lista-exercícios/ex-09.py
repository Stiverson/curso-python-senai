# Faça um programa que peça as 4 notas de 10 alunos, calcule a armazene em
# um vetor a média de cada aluno, imprima o número de alunos com média
# maior ou igual a 7.0.


num_alunos = 10
num_notas = 4

medias = []

for aluno in range(num_alunos):
    soma_notas = 0
    print(f"Aluno {aluno+1}:")
    for nota in range(num_notas):
        nota = float(input(f"Digite a nota {nota+1}: "))
        soma_notas += nota
    media = soma_notas / num_notas
    medias.append(media)

# Contando alunos com média >= 7.0
alunos_aprovados = sum(1 for media in medias if media >= 7.0)

print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")