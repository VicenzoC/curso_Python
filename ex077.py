tupla = ('APRENDER', 'CONHECER', 'ANDAR', 'CORRER', 'PEDALAR')
for palavra in tupla:
    print(f'\nNa palavra {palavra}, temos ',end='')
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra, end=' ')