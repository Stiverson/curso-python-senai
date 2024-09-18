meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
          "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

numeroMes = int(input("Digite o número do mês desejado: "))

if 1 <= numeroMes <= 12:
    print(f"O mês digitado é {meses[numeroMes-1]}")
else:
    print("Mês inválido, digite um valor entre 1 e 12!")