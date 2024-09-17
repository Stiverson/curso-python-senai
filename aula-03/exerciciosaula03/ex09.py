genero = str(input("Qual é o seu gênero ? Masculino (M) ou Feminino (F)? "))
altura = float(input("Digite a sua altura: "))

peso_ideal_m = (72.7 * float(altura)) - 58
peso_ideal_f = (62.1 * float(altura)) - 44.7

if genero == "M":
    print("Seu peso ideal é %.2f: " % peso_ideal_m)
elif genero == "F":
    print("Seu peso idela é %.2f: " % peso_ideal_f)
else:
    print("Gênero não definido!")