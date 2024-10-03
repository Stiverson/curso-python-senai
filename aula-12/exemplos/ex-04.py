def divi2(n1, n2):
    try:
        return float(n1) / float(n2)
    except ZeroDivisionError:
        print("Divisão por zero, operação inválida")
        return None

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um outro número: "))

resp = divi2(n1, n2)

if resp == None:
    print()
else:
    print("O resultado da divisão foi: ", resp)