peso = float(input("Digite o peso dos peixes: "))

limiteKilo = 50
multaPorKilo = 4.0
excesso = 0.0

if float(peso) > limiteKilo:
    excesso = (float(peso) - limiteKilo) * multaPorKilo
    print("O valor da multa eh de R$ %.2f " % excesso)
else:
    excesso = 0
    print("Excesso: %.2f" % excesso)