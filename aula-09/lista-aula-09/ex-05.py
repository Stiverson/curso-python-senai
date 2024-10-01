# Reverso do número. Faça uma função que retorne o reverso de um número inteiro
# informado. Por exemplo: 127 -&gt; 721. Além da função, faça com que o programa
# execute a função criada.


def inverter_numero(numero):
  """Inverte os dígitos de um número inteiro.

  Args:
    numero: O número inteiro a ser invertido.

  Returns:
    O número com os dígitos invertidos.
  """

  # Converte o número para uma string
  numero_str = str(numero)
  
  # Inverte a string
  numero_invertido_str = numero_str[::-1]
  
  # Converte a string invertida de volta para um número inteiro
  numero_invertido = int(numero_invertido_str)

  return numero_invertido

# Exemplo de uso
numero = int(input("Digite um número: "))
resultado = inverter_numero(numero)
print(f"O número invertido é: {resultado}")