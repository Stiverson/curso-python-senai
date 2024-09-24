a1 = 5 # Variavel global

def muda_e_imprime():
    a2 = 7 #Variavel Local
    print("A dentro da função: %d" % a2)

# Imprime o valor da variavel global

print("A antes de mudar: %d" % a1)

# Imprime o valor da variavel local

muda_e_imprime()

# imprime o valor de variavel global

print("A depois de mudar:  %d" % a1)