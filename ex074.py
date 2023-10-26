import random
tupla = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
print(f'Os números sorteados foram {tupla[0]}, {tupla[1]}, {tupla[2]}, {tupla[3]}, {tupla[4]}')
max = max(tupla)
min = min(tupla)
print(f'O menor é \033[33m{min}\033[m e o maior é \033[34m{max}')