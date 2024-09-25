base = float(input("Digite a base do triângulo  : "))
altura = float(input("Digite a altura do triângulo  : "))


def área_triângulo(base, altura):
    return (base * altura) / 2

print("A área do triângulo digitado é {} ".format(área_triângulo(base,altura)))