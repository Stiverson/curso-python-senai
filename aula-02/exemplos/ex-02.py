primeiraNota = int(input('Digite a primeira nota do aluno: '))
segundaNota = int(input('Digite a segunda nota do aluno: '))
terceiraNota = int(input('Digite a terceira nota do aluno: '))


media = (primeiraNota + segundaNota + terceiraNota) / 3

if media >= 9 :
   print(f'O conceito da media doa aluno  é: { media }','A')
elif media >= 7.5 and media <= 9 :
   print(f'O conceito da media doa aluno  é: { media }','B')
elif media >= 6 and media <= 7.5 :
   print(f'O conceito da media doa aluno  é: { media }','C')
elif media >= 4 and media <= 6 :
   print(f'O conceito da media doa aluno  é: { media }','D')
elif media < 4:
   print(f'O conceito da media doa aluno  é: { media }','E')