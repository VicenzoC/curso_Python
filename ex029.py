km = int(input('Qual a velocidade do carro? '))
if km > 80:
    print('Você foi multado!')
    multa = (km - 80) * 7
    print('O valor da multa será de R${:.2f}'.format(multa))
else:
    print('Você obedeceu as leis de trânsito e não foi multado,\nParabéns continue assim!')
