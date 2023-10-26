numeros = list()
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado com sucesso!')
    else:
        print('Esse número já existe, tente outro.')
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua != 'S':
        break
numeros.sort()
print(numeros)
