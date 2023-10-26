import math
ang = float(input('Digite um ângulo para saber seu sen, cos, e tan: '))
angR = ang * math.pi / 180
sen = math.sin(angR)
cos = math.cos(angR)
tan = math.tan(angR)
print('O ângulo de {}° tem\n{:9} = {:.2f}\n{:9} = {:.2f}\n{:9} = {:.2f}'.format(ang, 'seno', sen,'cosseno', cos,'tangente', tan))
