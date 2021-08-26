def dobro(n=0, f=False):
    res = n * 2
    if f:
        res = f'R${n:.2f}'.replace('.', ',')         # eu fiz assim, metodo menos eficiente
    return res                                       # o metodo melhor esta nas outras funções


def metade(n=0, f=False):
    res = n / 2
    return res if f is False else moeda(res)


def aumentar(n=0, p=0, f=False):
    res = n + ((n / 100) * p)
    return res if f is False else moeda(res)


def diminuir(n=0, p=0, f=False):
    res = n - ((n / 100) * p)
    return res if f is False else moeda(res)


def moeda(n=0):
    res = f'R${n:.2f}' .replace('.', ',')

    return res
