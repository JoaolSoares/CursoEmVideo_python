from random import randint
from time import sleep


def sorteio(lista):
    lista.clear()
    print(f'Nunmeros sorteados: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print()


def somapar(lista):
    soma = 0
    print(f'A soma de todos os numeros pares de ', end='')
    for c, n in enumerate(lista):
        if n % 2 == 0:
            soma += n
        print(f'{n}', end=' ')
    print(f'é igual a: {soma}')


numeros = list()
sorteio(numeros)
somapar(numeros)
