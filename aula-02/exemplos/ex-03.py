peso = float(input('Digite o seu peso separado por virgula : '))
altura = float(input('Digite sua altura separada por virgula: '))



imc = peso / (altura*altura)

if imc  <=19 and peso >=0 :
   print(f'O conceito da media doa aluno  é: { imc }','A')
elif imc >= 7.5 and imc <= 9 :
   print(f'O conceito da media doa aluno  é: { imc }','B')
elif imc >= 6 and imc <= 7.5 :
   print(f'O conceito da media doa aluno  é: { imc }','C')
elif imc >= 4 and imc <= 6 :
   print(f'O conceito da media doa aluno  é: { imc }','D')
elif imc < 4:
   print(f'O conceito da media doa aluno  é: { imc }','E')