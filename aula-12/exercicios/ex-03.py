# Crie um programa que leia uma lista de números e tente acessar um índice
# especificado pelo usuário, tratando a exceção de índice fora do intervalo.

def acessar_elemento_lista():
  lista = [1, 2, 3, 4]
  try:
    indice = int(input("Digite o índice a ser acessado: "))
    elemento = lista[indice]
    print(f"O elemento no índice {indice} é: {elemento}")
  except IndexError:
    print("Índice fora do intervalo da lista.")

acessar_elemento_lista()