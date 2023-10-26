#fatorial
n = int(input('Digite um número: '))
contf = 1
fat = n
while contf < n:
    fat *= (n - contf)
    contf += 1
print('O fatorial de {} é {}'.format(n, fat))
