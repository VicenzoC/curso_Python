#Progressão aritmetica v2.0
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
contadortermos = 0
while contadortermos != 10:
    pa = pt + r * contadortermos
    contadortermos += 1
    print('\033[34m{}\033[m'.format(pa), end=' -> ')
print('Fim')