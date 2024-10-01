# Reverso do número. Faça uma função que retorne o reverso de um número inteiro
# informado. Por exemplo: 127 -&gt; 721.

def inverter_numero(numero):
  # """Inverte os dígitos de um número inteiro.

  # Args:
  #   numero: O número inteiro a ser invertido.

  # Returns:
  #   O número com os dígitos invertidos.
  # """

  # Convertendo o número para string
  numero_str = str(numero)

  # Invertendo a string
  numero_invertido_str = numero_str[::-1]

  # Convertendo a string de volta para número
  numero_invertido = int(numero_invertido_str)

  return numero_invertido

# Exemplo de uso
numero = 127
resultado = inverter_numero(numero)
print(resultado)  # Saída: 721