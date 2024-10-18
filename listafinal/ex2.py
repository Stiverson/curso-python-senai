# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-
# matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa

# Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def saudacoes_estudo(turno):
  
  if turno.upper() == 'M':
    print("Bom Dia! Uma boa manhã de estudos!")
  elif turno.upper() == 'V':
    print("Boa Tarde! Uma boa tarde estudos!")
  elif turno.upper() == 'N':
    print("Boa Noite! Uma boa noite de estudos!")
  else:
    print(f"Valor Inválido!  Não conheço esse turno. Digite M, V ou N.")

while True:
  turno = input("Em que turno você estuda? (M-matutino, V-Vespertino, N-Noturno): ")
  saudacoes_estudo(turno)

  resposta = input("Deseja verificar outro turno? (S/N): ")
  if resposta.upper() != 'S':
    break 

print("Até mais! Bons estudos!")