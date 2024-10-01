# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e
# a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você
# deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados
# alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a
# descrição acima informada (retirar o melhor e o pior salto e depois calcular a média
# com as notas restantes). As notas não são informadas ordenadas. Um exemplo de
# saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7
# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9.04

def calcular_media_ginastica(nome, notas):
  # """Calcula a média de um ginasta, descartando a melhor e a pior nota.

  # Args:
  #   nome: O nome do ginasta.
  #   notas: Uma lista com as 7 notas do ginasta.

  # Returns:
  #   Uma tupla com o nome do ginasta, a melhor nota, a pior nota e a média final.
  # """

  # Ordenar as notas
  notas_ordenadas = sorted(notas)

  # Remover a melhor e a pior nota
  notas_validas = notas_ordenadas[1:-1]

  # Calcular a média
  media = sum(notas_validas) / len(notas_validas)

  return nome, notas_ordenadas[-1], notas_ordenadas[0], media

# Entrada de dados (exemplo)
nome_ginasta = "Aparecido Parente"
notas = [9.9, 7.5, 9.5, 8.5, 9.0, 8.5, 9.7]

# Chamada da função e exibição do resultado
resultado = calcular_media_ginastica(nome_ginasta, notas)
print("Atleta:", resultado[0])
print("Melhor nota:", resultado[1])
print("Pior nota:", resultado[2])
print("Média:", resultado[3])