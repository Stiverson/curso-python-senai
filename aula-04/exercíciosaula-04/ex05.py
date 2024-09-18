kilowatts = int(input("Quantos kilowatts você utilizou este mês: "))

if kilowatts >= 500:
    preco = 0.40

if kilowatts <= 1000:
        preco = 0.65
if kilowatts >= 2500:
        preco = 0.55
if kilowatts <= 5000:
        preco = 0.60
if kilowatts >= 1000:
       preco = 0.55
if kilowatts >= 1500:
       preco = 0.55

total_pagar = kilowatts * preco

print ("Você vai pagar este mês: R$%6.2f" % total_pagar)