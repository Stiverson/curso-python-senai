valorCasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário: "))
anos = int(input("Quantos anos para pagar: "))
meses = anos * 12
prestacao = valorCasa / meses

if prestacao > salario * 0.3:
    print("Você não pode obter o empréstimo")
else:
    print(f"Valor da prestação: R$ {prestacao:7.2f} Empréstimo OK")