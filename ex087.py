'''matriz= [[], [], []]
sompar = maxseg = 0
for n in range(0, 9):
    if n < 3:
        numero = int(input(f'Digite um número [0, {n}]: '))
        matriz[0].append(numero)
    elif 3 <= n < 6:
        numero = int(input(f'Digite um número [1, {n - 3}]: '))
        matriz[1].append(numero)
    elif 5 < n:
        numero = int(input(f'Digite um número [2, {n - 6}]: '))
        matriz[2].append(numero)
print(f"""
 [ {matriz[0][0]:^5} ][ {matriz[0][1]:^5} ][ {matriz[0][2]:^5} ]
 [ {matriz[1][0]:^5} ][ {matriz[1][1]:^5} ][ {matriz[1][2]:^5} ]
 [ {matriz[2][0]:^5} ][ {matriz[2][1]:^5} ][ {matriz[2][2]:^5} ]""")
for l in matriz:
    for a in l:
        if a % 2 == 0:
            sompar += a
        if l.index(a) == 1:
            if a > maxseg:
                maxseg = a
somterc = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A) A soma dos pares é {sompar}\n'
      f'B) A soma da terceira coluna é {somterc}\n'
      f'C) O maior número da segunda coluna é {maxseg}')'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somatercol = maior = 0
for rep in range(0, 2):
    for linha in range(0, 3):
        for coluna in range(0, 3):
            if rep == 0:
                matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}] '))
                if matriz[linha][coluna] % 2 == 0:
                    somapar += matriz[linha][coluna]
                if coluna == 2:
                    somatercol += matriz[linha][coluna]
                if linha == 1:
                    if coluna == 0 or matriz[linha][coluna] > maior:
                        maior = matriz[linha][coluna]
            else:
                print(f'[{matriz[linha][coluna]:^5}]', end='')
        print()
print(f'''A) A soma dos pares é {somapar}
B) A soma da terceira coluna é {somatercol}
C) O maior número da segunda linha é {maior}''')
