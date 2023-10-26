km = int(input('Quantos km tem sua viagem? '))
if km > 200:
    valor = km * 0.45
else:
    valor = km * 0.5
print('O valor da sua passagem vai ser de R${:.2f}'.format(valor))