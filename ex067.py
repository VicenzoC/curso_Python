while True:
    n = int(input('Digite um número para ver sua tabuada (0 para sair): '))
    if n == 0:
        break
    else:
        for t in range(1, 11):
            tabuada = n * t
            print(f'{n} x {t} = {tabuada}')
print('Encerrando programa...')
