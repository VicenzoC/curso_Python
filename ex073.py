tupla = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Corinthians', 'Fluminense', 'Atlético-GO', 'Athletico-PR', 'Ceará SC', 'Cuiabá', 'Internacional', 'Juventude', 'Santos', 'São Paulo', 'Bahia', 'América-MG', 'Sport Recife', 'Grêmio', 'Chapecoense')
print('A) Os primerios 5 colocados foram: ')
for top5 in range(0, 5):
    print(f'{top5 + 1}º colocado: {tupla[top5]}')
print('\nB) Os últimos 4 colocados foram: ')
for untop4 in tupla[-4:]:
    print(f'{tupla.index(untop4) + 1}º colocado: {untop4}')
print(f'\nC) Tupla em ordem alfabética:\n{sorted(tupla)}')
print(f'\nD) O chapecoense está em {tupla.index("Chapecoense") + 1}º colocado na tabela.')
