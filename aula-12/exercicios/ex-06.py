def divi2(n1):
    try:
        return float(n1)
    except ValueError:
        print("numero errado")
        return None

n1 = int(input("Digite um número decimal: "))


resp = divi2(n1)

if resp == None:
    print()
else:
    print("O numero digitado convertido é : ", resp)