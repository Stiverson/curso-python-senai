# Faça um programa que leia um número indeterminado de valores, correspondentes a
# notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que
# não deve ser armazenado). Após esta entrada de dados, faça:
# a. Mostre a quantidade de valores que foram lidos;
# b. Exiba todos os valores na ordem em que foram informados, um ao lado do
# outro;
# c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo
# do outro;
# d. Calcule e mostre a soma dos valores;
# e. Calcule e mostre a média dos valores;
# f. Calcule e mostre a quantidade de valores acima da média calculada;
# g. Calcule e mostre a quantidade de valores abaixo de sete;
# h. Encerre o programa com uma mensagem;

def analisar_notas():
   
    # Lê notas do usuário até que -1 seja informado e realiza diversas análises.
   

    notas = []
    while True:
        nota = float(input("Digite uma nota (ou -1 para encerrar): "))
        if nota == -1:
            break
        notas.append(nota)

    # a. Quantidade de valores lidos
    quantidade_notas = len(notas)
    print(f"Quantidade de notas: {quantidade_notas}")

    # b. Valores na ordem informada
    print("Valores na ordem informada:", end=" ")
    for nota in notas:
        print(f"{nota:.2f}", end=" ")
    print()

    # c. Valores na ordem inversa
    print("Valores na ordem inversa:")
    for nota in reversed(notas):
        print(f"{nota:.2f}")

    # d. Soma dos valores
    soma = sum(notas)
    print(f"Soma dos valores: {soma:.2f}")

    # e. Média dos valores
    media = soma / quantidade_notas
    print(f"Média dos valores: {media:.2f}")

    # f. Quantidade de valores acima da média
    acima_media = sum(1 for nota in notas if nota > media)
    print(f"Quantidade de valores acima da média: {acima_media}")

    # g. Quantidade de valores abaixo de sete
    abaixo_sete = sum(1 for nota in notas if nota < 7)
    print(f"Quantidade de valores abaixo de sete: {abaixo_sete}")

    print("Programa encerrado.")

# Chamada da função
analisar_notas()