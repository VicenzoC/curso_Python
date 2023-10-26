n = nmax = nmin = cont = soma = 0
p = 'S'
while p in 'Ss':
    n = int(input('Digite um valor: '))
    soma += n
    if cont == 0:
        nmax = n
        nmin = n
    else:
        if n > nmax:
            nmax = n
        if n < nmin:
            nmin = n
    p = input('Quer continuar? ').strip().upper()[0]
    cont += 1
m = soma / cont
print('O maior valor foi {}\nO menor valor foi {}\nA média dos {} números é de {}'.format(nmax, nmin, cont, m))
