soma = 0  
for num in range(1, 501):  
    if num % 2 != 0:  
        if num % 3 == 0:  
            soma += num  
print("A soma dos múltiplos é: {}.".format(soma))