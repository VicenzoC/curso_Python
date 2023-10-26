#programa calculadora
n1 = int(input('Digite um número(1)? '))
n2 = int(input('Digite um número(2)? '))
e = 0
r = 0
v = ''
while e != 8:
    e = int(input('''\n\n\nEscolha uma opção:
    
    [1] (+)   [2] (-) 
    --------------------
    [3] (/)   [4] (*)
    --------------------
    [5] (max) [6] (min)
    --------------------
    [7] novos números
    --------------------
    [8] sair do programa
    
    Digite sua escolha: \n'''))
    if e != 8:
        if e == 1:
            r = n1 + n2
            print('{} + {} = {}'.format(n1, n2, r))
        elif e == 2:
            r = n1 - n2
            print('{} - {} = {}'.format(n1, n2, r))
        elif e == 3:
            r = n1 / n2
            print('{} / {} = {}'.format(n1, n2, r))
        elif e == 4:
            r = n1 * n2
            print('{} * {} = {}'.format(n1, n2, r))
        elif e == 5:
            if n1 > n2:
                r = n1
                v = '>'
                print('{} {} {} então o maior é {}'.format(n1, v, n2, r))
            elif n1 < n2:
                r = n2
                v = '<'
                print('{} {} {} então o maior é {}'.format(n1, v, n2, r))
            else:
                r = 'Os dois são iguais'
                print('{} = {}'.format(n1, n2))
        elif e == 6:
            if n1 > n2:
                r = n2
                v = '>'
                print('{} {} {} então o menor é {}'.format(n1, v, n2, r))
            elif n1 < n2:
                r = n1
                v = '<'
                print('{} {} {} então o menor é {}'.format(n1, v, n2, r))
            else:
                r = 'Os dois são iguais'
                print('{} = {}'.format(n1, n2))
        elif e == 7:
            n1 = int(input('Digite o novo número(1)? '))
            n2 = int(input('Digite o novo número(2)? '))
        else:
            print('Dígito inválido, tente novamente.')
print('Terminando o programa...')
