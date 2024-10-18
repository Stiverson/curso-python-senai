# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas,
# com um número em cada posição e no qual a soma das linhas, colunas e
# diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com
# números de 1 a 9:
# 8 3 4
# 1 5 9
# 6 7 2
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos
# com as características acima. Dica: produza todas as combinações possíveis e
# verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece
# ser mais simples que usar uma matriz 3x3.

import itertools

def verificaQuadrado(quadrado):
    
    soma = sum(quadrado[0]) 
    for linha in quadrado:
        if sum(linha) != soma:
            return False
    for coluna in range(3):
        if sum(quadrado[i][coluna] for i in range(3)) != soma:
            return False
  
    if sum(quadrado[i][i] for i in range(3)) != soma:
        return False
    if sum(quadrado[i][2-i] for i in range(3)) != soma:
        return False
    return True

def encontra_quadrados():
   
    listaQuadrado = []
    for permutacao in itertools.permutations(range(1, 10)):
        quadrado = [permutacao[:3], permutacao[3:6], permutacao[6:]]
        if verificaQuadrado(quadrado):
            listaQuadrado.append(quadrado)
    return listaQuadrado


quadrados = encontra_quadrados()
print("Numero do quadrado  encontrados:")
for quadrado in quadrados:
    print(quadrado)