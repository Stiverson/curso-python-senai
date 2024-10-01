# Faça um programa em linguagem Python, que lê um número n e imprime os n
# primeiros números da sequência de Fibonacci.

fibo = [1,1]
i = 0
num = int(input("Entre com um número: "))

while num > len(fibo):
	fibo.append(fibo[i] + fibo[i+1])
	i+=1

print (f'Fibonacci de  {num} : {fibo} {num}-1' )