tupla = (int(input('Digite um número (1): ')), int(input('Digite um número (2): ')),
         int(input('Digite um número (3): ')), int(input('Digite um número (4): ')))
print(f'A) O valor 9 apareceu {tupla.count(9)} vezes.')
if tupla.count(3) > 0: # if 3 in tupla:
    print(f'B) O primeiro valor 3 apareceu na posição {tupla.index(3) + 1}.')
else:
    print('B) O valor 3 não apareceu na tupla.')
print('C) Os números pares foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')