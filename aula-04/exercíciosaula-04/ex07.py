idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso em kg: "))
horas_sono = float(input("Quantas horas você dormiu nas últimas 24 horas? "))

if 16 <= idade <= 69:
    if peso > 50:
        if horas_sono >= 6:
            print("Você pode doar sangue")
else:
    print("Voce Não Pode doar Sangue")