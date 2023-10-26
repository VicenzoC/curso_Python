import datetime

data = int(input('Qual ano você nasceu? '))
idade = datetime.date.today().year - data
if idade < 18:
    t = 18 - idade
    m = 'Fatam {} anos para você se alistar.'.format(t)
elif idade > 18:
    t = idade - 18
    ano18 = data + 18
    m = 'Já passaram {} anos do seu alistamento!\nSeu ano de alistamento foi {}.'.format(t, ano18)
else:
    m = 'Se aliste imediatamente!'
print(m)