kg = float(input('Quanto você pesa em Kg? '))
alt = float(input('Qual sua altura em Metro? '))
imc = kg / (alt**2)
if imc < 18.5:
    p = 'abaixo do peso'
elif 18.5 <= imc < 25:
    p = 'com peso normal'
elif 25 <= imc < 30:
    p = 'com sobrepeso'
elif 30 <= imc < 35:
    p = 'com obesidade (grau I)'
elif 35 <= imc < 40:
    p = 'com obesidade severa (grau II)'
elif imc >= 40:
    p = 'com obesidade mórbida (grau III)'
else:
    print('Valores inválidos, tente novamente.')
    exit()
print('Seu imc é de {:.2f}'.format(imc))
print ('você está {}.'.format(p))
