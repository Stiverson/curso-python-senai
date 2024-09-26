# A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T =
# [-10, -8, 0 1, 2, 5, -2, -4]. Faça um programa que imprima a maior e a menor
# temperatura, assim como a temperatura média.

temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4]


maior_temperatura = max(temperaturas)


menor_temperatura = min(temperaturas)


temperatura_media = sum(temperaturas) / len(temperaturas)


print("A maior temperatura é:", maior_temperatura)
print("A menor temperatura é:", menor_temperatura)
print("A temperatura média é:", temperatura_media)