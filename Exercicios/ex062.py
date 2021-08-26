pt = int(input('Diga o primeiro termo da P.A: '))
rz = int(input('Diga a tazão dessa P.A: '))

cont = 1
termo = pt
mais = 1

while mais != 0:
    while cont <= 9 + mais:
        print(termo, end=' - ')
        termo += + rz
        cont += 1

    print('Finish...')
    print('--' * 25)

    mais = int(input('Voce quer mostras mais quantos termos? '))

print('Finish...')
print('foi finalizado mostrando no final {} termos' .format(cont))
