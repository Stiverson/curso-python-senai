dias = input("Digite uma quantidade de dias: ")
horas = input("Digite uma quantidade de horas: ")
minutos = input("Digite uma quantidade de minutos: ")
segundos = input("Digite uma quantidade de segundos: ")

totalSegundos = (dias*24*60*60) + (horas*60*60) + (minutos*60) + segundos

print(dias,"dias",horas,"horas",minutos,"minutos",segundos,"segundos representam", totalSegundos,"segundos")
