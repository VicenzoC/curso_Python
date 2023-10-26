#numero
contador = 0
n = int(input('Digite um número: '))
for primo in range(1, n + 1):
    if n % primo == 0:
        print('\033[31m{}\033[m'.format(primo), end=' ')
        contador += 1
    else:
        print('\033[32m{}\033[m'.format(primo), end=' ')
if contador > 2:
    print('\nNão é primo')
else:
    print('\nÉ primo')
