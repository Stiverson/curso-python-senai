# Faça um programa que calcule a média ponderada de um aluno. Leia três notas, a
# primeira nota tem peso 2, a segunda nota tem peso 3 e a terceira nota tem peso 5.
# Calcule a média ponderada e imprima o resultado na tela. Considere que cada nota
# pode ir de 0 a 10.0.

def calcular_media_ponderada():
    """Calcula a média ponderada de um aluno com pesos 2, 3 e 5.

    Retorna:
        A média ponderada do aluno.
    """

    # Solicita as notas ao usuário
    nota1 = float(input("Digite a primeira nota (peso 2): "))
    nota2 = float(input("Digite a segunda nota (peso 3): "))
    nota3 = float(input("Digite a terceira nota (peso 5): "))

    # Validação das notas (opcional)
    if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or nota3 < 0 or nota3 > 10:
        print("As notas devem estar entre 0 e 10.")
        return

    # Cálculo da média ponderada
    media_ponderada = (nota1 * 2 + nota2 * 3 + nota3 * 5) / (2 + 3 + 5)

    # Imprime o resultado
    print(f"A média ponderada do aluno é: {media_ponderada:.2f}")

# Chama a função para calcular a média
calcular_media_ponderada()