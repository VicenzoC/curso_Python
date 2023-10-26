#seq fibonacci v1.0
n = int(input('Digite um número: '))
cont = 1
n1 = 0
n2 = 0
n3 = 0
while cont < n:
    if cont == 1:
        n1 = 0
        n2 = 1
        n3 = 1
        print('-> {}'.format(n1), end=' ')
    else:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    print('-> {}'.format(n3), end=' ')
    cont += 1
