frase = str(input('Digite uma frase que utilize parênteses: ')).strip()
contpe: int = frase.count('(')
contpd: int = frase.count(')')
indpe = 0
indpd = 0
if contpe == contpd > 0:
    for c in range(0, contpe):
        if c == 0:
            indpe = frase.index('(')
            indpd = frase.index(')')
            if indpe > indpd:
                print('Frase inválida')
                exit()
        else:
            indpe = frase.index('(', indpe + 1)
            indpd = frase.index(')', indpd + 1)
            if indpe > indpd:
                print('Frase inválida')
                exit()
    print('Frase válida.')
else:
    print('Frase inválida.')