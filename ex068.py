import random
cont = 0
while True:
    pi = str(input('Par ou Ímpar? ')).strip().upper()[0]
    jp = int(input('Escolha um número de 1 a 10: '))
    jc = random.randint(1, 10)
    soma = jp + jc
    if soma % 2 == 0:
        r = 'P'
    else:
        r = 'I'
    if pi == r:
        print(f'Você ganhou!\nJogada do computador: {jc}\nSua jogada: {jp}\nSoma = {soma}')
        cont += 1
    else:
        break
print(f'Jogada do computador: {jc}\nSua jogada: {jp}\nSoma = {soma}\nVocê perdeu depois de {cont} vitórias consecutivas!\nTente novamente!')