times = ('Atletico Mineiro', 'Flamengo', 'São Paulo', 'Internacional',
         'Fluminense', 'Palmeiras', 'Santos', 'Gremio', 'Fortaleza',
         'Corinthians', 'Atletico Paranaense', 'Bahia', 'Atletico goianiense',
         'Bragantino', 'Ceara', 'Sport', 'Vasco', 'Coritiba', 'Botafogo', 'Goias')

print('\033[1;34m----- Colocação Brasileirão 2020 -----\033[m')
print(' / '.join(times))

print('\033[1;32m--\033[m' * 30)
print('\033[1;34mOs 5 primeiros colocados:\033[m')
print(' / '.join(times[0:5]))

print('\033[1;32m--\033[m' * 30)
print('\033[1;34mOs 5 ultimos colocados:\033[m')
print(' / '.join(times[-5:]))

print('\033[1;32m--\033[m' * 30)
print('\033[1;34mOrdem alfabetica:\033[m')
print(' / '.join(sorted(times)))

print('\033[1;32m--\033[m' * 30)
print('\033[1;34mPosição do Corinthias:\033[m')
print('{} Colocado' .format(times.index('Corinthians') + 1))
