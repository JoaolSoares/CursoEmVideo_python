from time import sleep


def cont(i, f, p):
    print(f'Contagem de {i} a {f} com o passo de {p}')
    if p == 0:
        p += 1
    if p < 0:
        for c in range(i, (f - 1), p):
            print(f'{c} -> ', end='')
            sleep(0.3)
    else:
        for c in range(i, (f + 1), p):
            print(f'{c} -> ', end='')
            sleep(0.3)
    print('FIM')
    print('-=' * 35)


# Principal
cont(1, 10, 1)
cont(10, 0, -2)

print('Agora é voce!! ')
cont(i=int(input(' -Inicio: ')),
     f=int(input(' -Fim: ')),
     p=int(input(' -Passo: ')))

print(' -- Finish --')
