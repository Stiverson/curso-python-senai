caracteres=[]

vogais=["a","e","i","o","u"]

contvogal = 0
x = 1
while x <= 10:
    entrada = input("Caractere %d: " %x)
    x += 1
    caracteres.append(entrada)
    if entrada in vogais:
        contvogal += 1
print (f"Foram lidas o total de {(len(caracteres))-contvogal} Consoantes: ")