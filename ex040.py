from time import sleep
nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
m = (nota1 + nota2) / 2
if m < 5:
    r = '\033[7;31mReprovado\033[m'
    c = '\033[31mEstude mais no próximo ano!\033[m'
elif 5 <= m <= 6.9:
    r = '\033[31mRecuperação\033[m'
    c = '\033[31mEssa foi por pouco, se empenhe mais para não reprovar!\033[m'
else:
    r = '\033[32mAprovado!\033[m'
    c = '\033[32mParabéns você passou!\033[m'
print('\033[34mAnalisando...\033[m')
sleep(3)
print('Seu status: {}\n{}'.format(r, c))
