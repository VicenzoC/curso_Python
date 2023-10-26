import datetime
dtnasc = input('Data de nascimento (YYYY-mm-dd): ')
nasc = datetime.datetime.strptime('{}'.format(dtnasc),'%Y-%m-%d')
atual = datetime.datetime.strptime('{}'.format(datetime.date.today()),'%Y-%m-%d')
qdia = int((atual - nasc).days)
idade = qdia // 365
if idade <= 9:
    c = 'Mirim'
elif 9 < idade <= 14:
    c = 'Infantil'
elif 14 < idade <= 19:
    c = 'Junior'
elif 19 < idade <= 25:
    c = 'Sênior'
else:
    c = 'Master'
print('Você tem {} anos, está na categoria {}.'.format(idade, c))
