a = 5 # Variavel global

def muda_e_imprime():
    global a # Variavel global
    a = 7
    print(" a dentro da função: %d" % a)