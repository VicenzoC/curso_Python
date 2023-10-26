import math

a = int(input('Digite um comprimento de reta(1): '))
b = int(input('Digite um comprimento de reta(2): '))
c = int(input('Digite um comprimento de reta(3): '))
if (b + c) > a > math.fabs(b - c) and (a + c) > b > math.fabs(a - c) and (a + b) > c > math.fabs(a - b):
    tri = 'Dá'
    if a == b != c or a == c != b or b == c != a:
        tip = 'Isóceles'
    elif a != b != c:
        tip = 'Escaleno'
    elif a == b == c:
        tip = 'Equilátero'
else:
    tri = 'Não dá'
    print('{} para fazer um triângulo, tente novamente'.format(tri))
    exit()
print('{} para fazer um triângulo, seu tipo será {}'.format(tri, tip))
