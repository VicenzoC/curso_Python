import math
cateto1 = float(input('Comprimento do cateto 1: '))
cateto2 = float(input('Comprimento do cateto 2: '))
hip = math.hypot(cateto1, cateto2)
print('A hipotenusa do triângulo é {}'.format(hip))
