dict = dict()
gols = []
total = 0

dict['nome'] = str(input('Nome do jogador: '))
dict['partidas'] = int(input(f'Quantas partidas {dict["nome"]} jogou? '))

for c in range(1, (dict['partidas'] + 1)):
    numgol = int(input(f'Gols na {c}º partida: '))
    gols.append(numgol)
    total += numgol

dict['gols'] = gols
dict['total'] = total

print('-=' * 30)
print(dict)

print('-=' * 30)
for k, v in dict.items():
    print(f'{k} é {v}')

print('-=' * 30)
print(f'O {dict["nome"]} Fez {dict["total"]} Gols em {dict["partidas"]} partidas!')

for c, n in enumerate(gols):
    print(f' ->Na {c + 1}º Partida, fez {n} Gols.')
