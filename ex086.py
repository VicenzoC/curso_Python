"""matriz= [[], [], []]
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
print(f"
 [ {matriz[0][0]} ][ {matriz[0][1]} ][ {matriz[0][2]} ]
 [ {matriz[1][0]} ][ {matriz[1][1]} ][ {matriz[1][2]} ]
 [ {matriz[2][0]} ][ {matriz[2][1]} ][ {matriz[2][2]} ]")"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for rep in range(0, 2):
    for linha in range(0, 3):
        for coluna in range(0, 3):
            if rep == 0:
                matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}] '))
            else:
                print(f'[{matriz[linha][coluna]:^5}]', end='')
        print()
