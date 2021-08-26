lista = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 50)
print('{:^50}' .format('LISTA DE PREÇOS'))
print('-' * 50)

for c in range(0, len(lista)):
    if c % 2 == 0:
        print('{:.<35}' .format(lista[c]), end='')

    elif c % 2 != 0:
        print(' R$: {:>6}'.format(lista[c]))

print('-' * 50)
