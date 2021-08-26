def dobro(n=0):
    res = n * 2
    return res


def metade(n=0):
    res = n / 2
    return res


def aumentar(n=0, p=0):
    res = n + ((n / 100) * p)
    return res


def diminuir(n=0, p=0):
    res = n - ((n / 100) * p)
    return res


def moeda(n=0):
    res = f'R${n:.2f}' .replace('.', ',')

    return res
