salario = float (input ("Informe o salário do funcionário : R$ "))

salario_minimo = float (input ("Informe o salário mínimo : R$ "))

quantidade = salario / salario_minimo

print(f"O funcionário ganha {quantidade:.0f} salários mínimos")