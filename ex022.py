nome = str(input('Qual seu nome? ')).strip()
NO = nome.split()
print(nome.upper())
print(nome.lower())
print('O nome inteiro, sem contar os espeços, tem {} caractéres'.format(len(nome)-nome.count(' ')))
print('O primeiro nome tem {} caractéres'.format(len(NO[0])))

