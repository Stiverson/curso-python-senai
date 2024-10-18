# Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘.
# Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por
# omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa
# forem informados, eles devem ser modificados para valores dentro da faixa de
# forma elegante.

import itertools

def desenha_retangulo(linhas=1, colunas=1):
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))
    print("+" + "-" * colunas + "+")
    for _ in range(linhas):
        print("|" + " " * colunas + "|")
    print("+" + "-" * colunas + "+")

def verificaQuadrado(quadrado):
    
    soma_quadrado = sum(quadrado[0])  
    
    for linha in quadrado:
        if sum(linha) != soma_quadrado:
            return False
    for i in range(3):
        if sum(quadrado[j][i] for j in range(3)) != soma_quadrado:
            return False
    if sum(quadrado[i][i] for i in range(3)) != soma_quadrado:
        return False
    if sum(quadrado[i][2-i] for i in range(3)) != soma_quadrado:
        return False
    return True

def encontra_quadrados():
    quadrados_magicos = []
    for permutacao in itertools.permutations(range(1, 10)):
        quadrado = [permutacao[:3], permutacao[3:6], permutacao[6:]]
        if verificaQuadrado(quadrado):
            quadrados_magicos.append(quadrado)
    return quadrados_magicos

desenha_retangulo(5, 10)