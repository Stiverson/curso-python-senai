# Escreva um programa, com uma função que imprima o conceito de um
# aluno, dada a sua nota. Supor, apenas, notas inteiras. O critério para
# conceitos é o seguinte:
# Notas inferiores a 3 Conceito E
# Notas de 3 a 5 Conceito D
# Notas de 6 a 7 Conceito C
# Notas de 8 a 9 Conceito B
# Nota 10  Conceito A

def calcula_conceito(media):
  
  if media < 3:
    return "E"
  elif 3 <= media <= 5:
    return "D"
  elif 6 <= media <= 7:
    return "C"
  elif 8 <= media <= 9:
    return "B"
  else:
    return "A"

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

conceito = calcula_conceito(media)

print(f"A média do aluno é {media} e o conceito é {conceito}.")