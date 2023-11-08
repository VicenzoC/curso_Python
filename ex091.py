import random
from operator import itemgetter

pontos = dict()
print('Valores Sorteados: ')
for i in range(1, 5):
    pontos[f'jogador{i}'] = random.randint(1, 6)
    print(f'    O jogador {i} tirou {pontos[f"jogador{i}"]}')

ranking = sorted(pontos.items(), key=itemgetter(1), reverse=True)

print('\nRanking dos jogadores: ')
for i, v in enumerate(ranking):
    print(f'    {i+1} lugar: {v[0]} com {v[1]}')
