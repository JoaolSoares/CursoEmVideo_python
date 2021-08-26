def fatorial(n, show=False):
    """
    :param n: Numero para saber seu fatorial
    :param show: True para mostrar resolução
    :return: resposta do fatorial de n
    """

    fat = 1
    for c in range(n, 0, -1):
        fat *= c
        if show is True:
            if c == n - (n - 1):
                print(c, end=' = ')
            else:
                print(c, end=' X ')
    return fat


def TF(res):
    if res[0] in 'Tt':
        return True
    else:
        return False


res1 = int(input('Digite um numero para saber o seu fatorial: '))
resfinal = TF(input('Saber o processo? [True/False]: '))

print('-=' * 20)
print(fatorial(res1, resfinal))
