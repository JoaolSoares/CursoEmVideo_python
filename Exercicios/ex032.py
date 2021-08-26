ano = int(input('Diga um ano: '))
bi = ano % 4
if bi == 0:
    print('É um ano bissexto')
else:
    print('Não é um ano bissexto')