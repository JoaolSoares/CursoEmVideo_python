def dobro(n=0, f=False):
    res = n * 2
    if f:
        res = f'R${res:.2f}'.replace('.', ',')         # eu fiz assim, metodo menos eficiente
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


def resumo(p=0, txa=0, txd=0):
    print()
    print('-' * 26)
    print('RESUMO DE PREÇO' .center(26))
    print('-' * 26)
    print(f'{"PREÇO ORIGINAL:":<18}{moeda(p)}')
    print(f'{"DOBRO DO PREÇO:":<18}{dobro(p, True)}')
    print(f'{"METADE DO PREÇO:":<18}{metade(p, True)}')
    print(f'{f"{txa}% DE AUMENTO:":<18}{aumentar(p, txa, True)}')
    print(f'{f"{txd}% DE DESCONTO:":<18}{diminuir(p, txd, True)}')
    print('-' * 26)
