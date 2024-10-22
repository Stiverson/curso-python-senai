def valida_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

   
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

   
    if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
        return True
    else:
        return False

cpf = input("Digite o CPF: ")
if valida_cpf(cpf):
    print("CPF válido")
else:
    print("CPF inválido")