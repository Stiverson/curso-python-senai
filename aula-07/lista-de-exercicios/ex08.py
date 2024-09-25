# Escreva um programa, com uma função para ler a idade de uma pessoa e
# informar a sua classe eleitoral, conforme:
# Não-eleitor – abaixo de 16 anos;
# Eleitor obrigatório – entre 18 e 65 anos;
# Eleitor facultativo – entre 16 e 18 ou maior de 65 anos.

def classifica_eleitor(idade):
 
  if idade < 16:
    return "Não-eleitor"
  elif 16 <= idade <= 18 or idade > 65:
    return "Eleitor facultativo"
  else:
    return "Eleitor obrigatório"

idade = int(input("Digite a sua idade: "))

classe_eleitoral = classifica_eleitor(idade)

print(f"Você é {classe_eleitoral}.")