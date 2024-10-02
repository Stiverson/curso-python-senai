# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
# perguntas são:
# a.Telefonou para a vítima
# b.Esteve no local do crime
# c.Mora perto da vítima
# d.Devia para a vítima
# e.Já trabalhou com a vítima
# O programa deve no final emitir uma classificação sobre a participação da pessoa no
# crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada
# comoSuspeit, entre 3 e 4 comoCúmplic e 5 comoAssassin. Caso contrário,
# ele será classificado como Inocente.


def classificar_suspeito():
  # Classifica um suspeito com base em suas respostas a perguntas sobre um crime.

  # Retorna:
  #   Uma string indicando a classificação do suspeito.
 

  # Lista de perguntas
  perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
  ]

  # Contador de respostas positivas
  respostas_positivas = 0

  # Faz as perguntas e conta as respostas positivas
  for pergunta in perguntas:
    resposta = input(pergunta + " (sim/não): ").lower()
    if resposta == "sim":
      respostas_positivas += 1

  # Classifica o suspeito
  if respostas_positivas == 5:
    return "Assassino"
  elif respostas_positivas >= 3:
    return "Cúmplice"
  elif respostas_positivas == 2:
    return "Suspeita"
  else:
    return "Inocente"

# Chama a função para classificar o suspeito
resultado = classificar_suspeito()
print(f"O suspeito é classificado como: {resultado}")