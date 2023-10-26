#Jokenpô
import random
from time import sleep
ljoga = ['Pedra', 'Papel', 'Tesoura']
jc = random.choice(ljoga) #jogada do computador
ep = int(input('Escolha uma ação:\n[0] = Pedra\n[1] = Papel\n[2] = Tesoura\nDigite sua escolha: ')) #jogada da pessoa
jp = ljoga[ep]
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(0.5)
print('{}\n{:^20}\033[32m{}\033[m\n{:^20}\033[32m{}\033[m\n{}'.format('=' * 40, 'O \033[31mcomputador\033[m jogou ', jc, '\033[34mVocê\033[m jogou ', jp, '=' * 40))
if jc == jp:
    r = '\033[34mEmpate!\033[m'
elif (jc == 'Pedra' and jp == 'Tesoura') or (jc == 'Papel' and jp == 'Pedra') or (jc == 'Tesoura' and jp == 'Papel'):
    r = '\033[31mPerdeu!\033[m'
elif (jp == 'Pedra' and jc == 'Tesoura') or (jp == 'Papel' and jc == 'Pedra') or (jp == 'Tesoura' and jc == 'Papel'):
    r = '\033[32mGanhou!\033[m'
print(r)