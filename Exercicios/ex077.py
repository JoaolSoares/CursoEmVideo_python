lista = ('joao', 'mariana', 'patricia', 'silvio', 'caio', 'debora', 'estojo',
         'lingua', 'cerebro')

for n in lista:
    print(f'\n{n} temos: ', end='')

    for letra in n:
        if letra.upper() in 'AEIOU':
            print(f'{letra}', end=' ')
