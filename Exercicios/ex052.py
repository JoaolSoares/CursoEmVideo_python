print('-' * 5, 'Identificador de numero primo', 5 * '-')

cont = 0
n1 = int(input('Diga um numero: '))

for c in range(1, n1 + 1):
    if n1 % c == 0 and n1 % n1 == 0:
        print('\033[1;34m', end='')
        cont += 1
    else:
        print('\033[1;37m', end='')
    print(c, end=' ')

if cont == 2:
    print('\n\033[1;32mÉ um numero primo\033[m')
    print('O numero pode ser dividido {} vezes' .format(cont))
else:
    print('\n\033[1;31mNão é um numero primo\033[m')
    print('O numero pode ser dividido {} vezes' .format(cont))
