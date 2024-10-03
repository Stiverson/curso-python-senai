while True:
    try:
        x = int(input("Digite um número inteiro: "))
        break
    except:
        print("Opa... Isso não é um número inteiro. Tente novamente...")

print("A entrada foi validada")