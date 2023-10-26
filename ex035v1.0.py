import math

a = int(input('Digite um comprimento de reta(1): '))
b = int(input('Digite um comprimento de reta(2): '))
c = int(input('Digite um comprimento de reta(3): '))
if (b + c) > a > math.fabs(b - c) and (a + c) > b > math.fabs(a - c) and (a + b) > c > math.fabs(a - b):
    tri = 'Dá'
else:
    '''if (a + c) > b > math.fabs(a - c):
        tri = 'Dá'
    else:
        if (a + b) > c > math.fabs(a - b):
            tri = 'Dá'
        else:'''
    tri = 'Não dá'
print('{} para fazer um triângulo com {}, {} e {}'.format(tri, a, b, c))
