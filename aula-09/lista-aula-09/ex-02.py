# Desenvolva um programa que armazene quatro notas em uma lista e que apresente a
# média final. Caso a média seja igual ou superior a 7, apresente a mensagem
# “APROVADO”, caso contrário, armazenar a nota da prova final e recalcular a média.
# Caso a nova média seja igual ou superior a 5, apresentar a mensagem “APROVADO”,
# caso contrário, apresentar a mensagem “REPROVADO”.



def calcular_media(notas):
  # Calcula a média de uma lista de notas.
  return sum(notas) / len(notas)

notas = []
for i in range(4):
  nota = float(input(f"Digite a {i+1}ª nota: "))
  notas.append(nota)

media_inicial = calcular_media(notas)

if media_inicial >= 7:
  print("APROVADO")
else:
  nota_final = float(input("Digite a nota da prova final: "))
  notas.append(nota_final)
  media_final = calcular_media(notas)

  if media_final >= 5:
    print("APROVADO")
  else:
    print("REPROVADO")