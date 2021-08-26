from time import sleep
from random import randint
from operator import itemgetter

valor = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
rank = []

print('-' * 11)
print(f'{" Dados ":-^11}')
print('-' * 11)
print()

for k, v in valor.items():
    print(f'- Dado do {k}: {v}')
    sleep(0.7)

print()
print('-- Ranks --')

rank = sorted(valor.items(), key=itemgetter(1), reverse=True)

sleep(0.7)
for i, v in enumerate(rank):
    print(f'{i + 1}º Lugar: {v[0]} com {v[1]}')
    sleep(0.7)
