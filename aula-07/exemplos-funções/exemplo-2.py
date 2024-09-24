def epar(x):
    return(x % 2 == 0)

def par_ou_impar(x):
    if epar(x):
        return "Esse numero é par"
    else:
        return "Esse numero é impar"
print(par_ou_impar(4))
print(par_ou_impar(5))