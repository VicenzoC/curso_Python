#jogo adivinha v1.0
import random
from time import sleep
ns = [0, 1, 2, 3, 4, 5]
n = random.choice(ns)
e = int(input('Tente adivinhar o número que estou pensando de 0 a 5\nEscolha um número: '))
print('ANALISANDO...')
sleep(3)
if n == e:
    print('você acertou!')
else:
    print('você errou, estava pensando no número {}.\nTente novamente.'.format(n))
