
while True:
    print('\033[1;35m' + '--' * 9)
    print('Sistema interativo')
    print('       de         ')
    print('     Pyhelp       ')
    print('--' * 9, '\033[m')

    res = str(input('\033[1;34m  -Função ou Biblioteca: [FIM para acabar]: \033[m'))

    if res.upper().strip() in 'FIM':
        break

    else:
        print('\033[1;30;47m')
        help(res)
        print('\033[m')

print('-' * 15)
print('\033[1;31mFinalizando...\033[m')

# ERA PRA BOTAR COR ATRAVEZ DE FUNÇÃO MAS NÃO TINHA ENTENDIDO
