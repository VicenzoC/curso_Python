import datetime
contmaior = 0
contmenor = 0
for p in range(1, 8):
    dt = int(input('Qual a data de nascimento da {}° pessoa? '.format(p)))
    if datetime.date.today().year - dt >= 18:
        contmaior += 1
    else:
        contmenor += 1
print('Temos {} maiores de idade e {} menores de idade'.format(contmaior, contmenor))
