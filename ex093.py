jogador = dict()
jogos = list()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(partidas):
    jogos.append(int(input(f'Quantos gols na partida {p + 1}? ')))
jogador['gols'] = jogos
jogador['total'] = sum(jogos)
print('-=' * 50)
print(jogador)
print('-=' * 50)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 50)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for p in range(partidas):
    print(f'    => Na partida {p + 1}, fez {jogador["gols"][p]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')