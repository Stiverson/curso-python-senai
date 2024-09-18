km = int(input("Qual a velocidade que você atingiu ??: "))

if km >= 80:
    multa = 5
    total_pagar = multa * km
    print ("Você foi multado o valor a  pagar este mês: R$%6.2f" % total_pagar)
else:
   print('Você não foi multado')



