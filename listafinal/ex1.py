# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
# que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7 * h) – 58
# Para mulheres: (62.1 * h) - 44.7
# OBS: Permitir que o usuário escolha entre os Gêneros para realizar o cálculo de
# acordo. Caso queira, pode realizar um Loop para verificar se o usuário quer realizar
# outro cálculo ou não.

def calcular_peso_ideal(altura, genero):
    if genero.upper() == 'M':
        peso_ideal = (72.7 * altura) - 58
    elif genero.upper() == 'F':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        return 

    return peso_ideal

def parar_calculo():
    global continuar_programa  
    continuar_programa = False

continuar_programa = True
while continuar_programa:
    altura = float(input("Digite a sua altura em metros ex:1.68 : "))
    genero = input("Digite o gênero (M/F): ")
    peso_ideal = calcular_peso_ideal(altura, genero)
    print("Seu peso ideal é:", peso_ideal)

    resposta = input("Deseja calcular novamente? (S/N): ")
    if resposta.upper() != 'S':
        parar_calculo()  