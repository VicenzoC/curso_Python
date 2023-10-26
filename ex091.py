import random

pontos = dict()
print('Valores Sorteados: ')
for i in range(1, 5):
    pontos[f'jogador{i}'] = random.randint(1, 6)
    print(f'    O jogador {i} tirou {pontos[f"jogador{i}"]}')


print('Ranking dos jogadores: ')
for i in range(1, 5):
    for k, v in pontos.items():
        print(f'{i} lugar: {k} com {v}')
