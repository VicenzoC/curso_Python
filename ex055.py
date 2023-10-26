pmax = 0
pmin = 0
for peso in range(1,6):
    p = float(input('Qual seu peso? (Kg) '))
    if peso == 1:
        pmax = p
        pmin = p
    else:
        if p > pmax:
            pmax = p
        if p < pmax:
            pmin = p
print('O menor peso foi de {}Kg e o maior peso foi de {}Kg.'.format(pmin, pmax))
