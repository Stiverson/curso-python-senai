salario = float(input("Qual o valor do seu salário: "))

if salario > 1250:
    aumento = 0.10
    valorAtual = salario * aumento
    resultado = valorAtual + salario
    print ("O seu salário atual é de : R$%6.2f" %resultado)
if salario <= 1250:
   aumentoInf = 0.15
   valorAtualInf = salario * aumentoInf
   resultado2 = valorAtualInf + salario
   print("O seu salário atual é de : R$%6.2f"  %resultado2)