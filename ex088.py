import random
from time import sleep
listajg = list()
jogo = list()
cont = 0
print('_' * 20)
print(f'{"MEGA SENA":^20}')
print('-' * 20)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
for j in range(0, quant):
    jogo.clear()
    cont = 0
    while True:
        if cont == 6:
            break
        else:
            n = random.randint(1, 60)
            if n not in jogo:
                jogo.append(n)
                cont += 1
    jogo.sort()
    listajg.append(jogo[:])
    sleep(1)
    print(f'Jogo {j + 1:<3}: {listajg[j]}')