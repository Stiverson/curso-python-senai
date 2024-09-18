idade = int(input("Digite a sua idade: "))
anoNascimento = int(input("Digite o ano de nascimento: "))

anoAtual = 2024

idadeEmanos = anoAtual - anoNascimento
idadeEmMeses = idadeEmanos * 12
idadeEmDias = idadeEmanos * 365
idadeEmSemanas = idadeEmDias / 4

print(f"Sua idade em anos é: {idadeEmanos}")
print(f"Sua idade em meses é: {idadeEmMeses}")
print(f"Sua idade em dias é: {idadeEmDias}")
print(f"Sua idade em semanas é: {idadeEmSemanas}")