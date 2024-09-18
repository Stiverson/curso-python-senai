numero1 = int(input("Digite o primeiro numero : "))
numero2 = int(input("Digite o segundo numero : "))

operacao = input("Digite a operação desejada (1)Adição, (2)Subtração (3)Multiplicação (4)Divisão:  ")


if operacao == "1":
    soma = numero1 + numero2
    print('O valor da sua operação é :',soma)
elif operacao == "2":
        sub = numero1 - numero2
        print('O valor da sua operação é :',sub)
elif operacao == "3":
        multi = numero1 * numero2
        print('O valor da sua operação é :',multi)
elif operacao == "4":
        div = numero1 / numero2
        print('O valor da sua operação é :',div)
else:
    print ("Categoria inválida, digite um valor entre 1 e 4!")
