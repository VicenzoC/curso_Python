num = list()
for n in range(1, 6):
    num.append(int(input(f'Digite um número ({n}): ')))
max = max(num)
min = min(num)

print(f'O maior número foi {max} e está na posição ', end='')
for ind, n in enumerate(num):
    if n == max:
        print(f'{ind + 1}', end=' ')
print(f'\nO menor número foi {min} e está na posição ', end='')
for ind, n in enumerate(num):
    if n == min:
        print(f'{ind + 1}', end=' ')

