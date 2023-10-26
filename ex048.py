somatorio = 0
contador = 0
for impar in range(1, 500, 2):
    if impar % 3 == 0:
        somatorio += impar #s = s + impar
        contador += 1
print('A soma dos {} valores que são ímpares, múltiplos de 3 e estão entre 1 e 500 = {}'.format(contador, somatorio))