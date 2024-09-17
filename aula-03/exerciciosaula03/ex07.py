qnt_ganha = float(input('Quanto ganha por hora? '))
horas_trabalhadas = int(input('Horas trabalhadas por mês: '))

salario_bruto = qnt_ganha * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

print ('+ Salário Bruto : R$ %.2f' %salario_bruto)
print ('- IR: R$ %.2f' %ir )
print ('- INSS: R$ %.2f' %inss )
print ('- Sindicato: R$ %.2f' %sindicato )
print ('= Salário Liquido : R$ %.2f' %(salario_bruto - ir - inss - sindicato))