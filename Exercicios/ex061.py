pt = int(input('Diga o primeiro termo da P.A: '))
rz = int(input('Diga a tazão dessa P.A: '))

cont = 1
termo = pt

while cont <= 10:
    print(termo, end=' - ')
    termo += + rz
    cont += 1

print('Finish...')
