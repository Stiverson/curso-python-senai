print("----------------  Calculos de valores ---------------------")

valorBruto = float(input('Quanto você ganha em valor bruto: R$  '))

if valorBruto <= 1903.98:
    faixa = 0
elif valorBruto >= 1903.99 and valorBruto <= 2826.65:
    faixa = 0.075
    deducao = 142.80
elif valorBruto >= 2826.66 and valorBruto <= 3751.05:
    faixa = 0.15
    deducao = 354.80
elif valorBruto >= 3751.06 and valorBruto <= 4664.68:
    faixa = 0.225
    deducao = 636.13  
elif valorBruto >= 4664.69:
    faixa = 0.275
    deducao = 869.36
else:
    print("Valor do salário fora da faixa de imposto de renda")       
            
if  faixa == 0:
    print(f"Salário líquido: R$ {valorBruto:.2f}")
    print("Insento de imposto de Renda") 
else:
    imposto_pagar = valorBruto * faixa
    imposto_retido = imposto_pagar - deducao

    salario_liquido = valorBruto - imposto_pagar - imposto_retido

    print()
    print("----------------    Resumo dos calculos ---------------------")  
    print(f"Salário Bruto :              R$ {valorBruto:.2f}")
    print(f"Porcentagem de imposto de renda:    {faixa:.1%}")
    print(f"Imposto a Pagar:             R$ {imposto_pagar:.2f}")
    print(f"Valor a ser deduzido :       R$ {deducao:.2f}  ")
    print(f"Valor do imposto retido na fonte :       R$ {imposto_retido:.2f}  ")
    print(f"Salario Líquido :            R$ {salario_liquido:.2f}  ")  
    print("----------------          Fim              ---------------------") 




