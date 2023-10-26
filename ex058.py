#jogo adivinha v2.0
import random
random.randint(0, 10)
jc = random.randint(0, 10)
ganhou = False
contjogada = 0
print('Pensei em um número entre 0 e 10, duvido você acertar!')
while not ganhou:
   jp = int(input('Qual número estou pensando? '))
   contjogada += 1
   if jp == (jc - 1) or jp == (jc + 1):
       print('Essa foi perto!!')
   if jp == jc:
       ganhou = True

print('Você acertou depois de {} tentativas'.format(contjogada))