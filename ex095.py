jogadores = list()
jogador = dict()
continua = ''
while continua != 'N':
    jogos = list()
    print('=' * 50)
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(partidas):
        jogos.append(int(input(f'Quantos gols na partida {p + 1}? ')))
    jogador['gols'] = jogos[:]
    jogador['total'] = sum(jogos)
    jogadores.append(jogador.copy())
    continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

print('-=' * 50)
print(jogadores)
print('-=' * 50)
print(f'{"cod":5}{"nome":15}{"gols":15}{"total":5}')
print('-'*40)
for i, j in enumerate(jogadores):
    print(f'''{i:<5}{j["nome"]:15}{f"{j['gols']}":15}{j["total"]:<5}''')

while True:
    cod = int(input('\nDigite o código do jogador para mais detalhes (999 para sair): '))
    if cod == 999:
        break
    elif cod < len(jogadores):
        print(f'\n-- LEVANTAMENTO DO JOGADOR {jogadores[cod]["nome"]} --')
        for i, p in enumerate(jogadores[cod]["gols"]):
            print(f'No jogo {i + 1} fez {p} gols')
    else:
        print('ERROR: CÓDIGO INVÁLIDO')