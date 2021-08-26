def titulo(txt):
    print()
    tamlin = len(txt) + 4
    print('-' * tamlin)
    print(f'{txt:^{tamlin}}')     # print(f'  {txt}')
    print('-' * tamlin)


titulo(str(input('Digite o titulo desejado: ')))
