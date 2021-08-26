def menu(titulo, *msgs):
    print('-' * 30)
    t1 = titulo.upper()
    print(f'{t1:^30}')
    print('-' * 30)

    for c, m in enumerate(msgs):
        print(f'  {c+1}) {m}')
    print('-' * 30)

    while True:
        try:
            res = int(input(' -Digite sua escolha: '))
        except (ValueError, KeyboardInterrupt):
            print('\033[1;31mERRO! O valor digitado não é valido, tente novamente...\033[m')
            print('\033[1;34mPara ver novamente as opções digite 999\033[m')
            print('-' * 10)
            continue

        else:
            if res == 999:
                print()
                print('-' * 30)
                t1 = titulo.upper()
                print(f'{t1:^30}')
                print('-' * 30)

                for c, m in enumerate(msgs):
                    print(f'  {c + 1}) {m}')
                print('-' * 30)
            elif res > len(msgs) or res <= 0:
                print('\033[1;31mERRO! Não encontrei a opção com este numero, tente novamente...\033[m')
                print('\033[1;34mPara ver novamente as opções digite 999\033[m')
                print('-' * 10)
                continue
            else:
                return res


def menusec(opc):
    print()
    print('-' * 30)
    print(f'{f"OPÇÃO {opc}":^30}')
    print('-' * 30)


def tabela(lista):
    print(f'{"NOME":<24}{"IDADE"}')
    print('-' * 30)
    for c, p in enumerate(lista):
        p = p.replace('\n', '')
        if c % 2 == 0:
            print(f'{p:<22}', end='')            # ele fez com dado = p.split(';') que da um espaço no ;
        else:
            print(f'{p:<} Anos')

