a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
if a > b and a > c:
    print('O maior número é {}'.format(a))
else:
    if b > a and b > c:
        print('O maior número é {}'.format(b))
    else:
        print('O maior número é {}'.format(c))
if a < b and a < c:
    print('O menor número é {}'.format(a))
else:
    if b < a and b < c:
        print('O menor número é {}'.format(b))
    else:
        print('O menor número é {}'.format(c))
