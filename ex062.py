#Progressão aritmetica v3.0
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
contadortermos = 0
qt = 10
while contadortermos != qt:
    pa = pt + r * contadortermos
    contadortermos += 1
    print('\033[34m{}\033[m'.format(pa), end=' -> ')
    if contadortermos == qt:
        qt += int(input('Quantos termos mais você quer ver? '))
print('Fim')