pt = int(input('Digite o valor do 1° termo: '))
r = int(input('Digite o valor da razão: '))
st = (pt + (10 * r))
for pa in range(pt, st, r):
    print(pa, end=' -> ')
print('Fim')