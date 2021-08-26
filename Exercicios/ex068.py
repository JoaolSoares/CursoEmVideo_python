from random import randint

print('--' * 12)
print('JOGO DO PAR OU IMPAR')

cont = 0
jog = ' '

while True:
    pc = randint(1, 10)
    jog = ' '

    while jog not in 'PpIi':
        print('--' * 12)
        jog = input('PAR ou IMPAR: ')[0].strip()

    player = int(input('Diga a sua jogada: '))
    print('--' * 12)

    if jog in 'Pp':

        if (player + pc) % 2 == 0:
            print(f'O computador jogou {pc} e vc jogou {player}')
            print('\033[1;32mVOCE GANHOU!!!!\033[m')
            cont += 1

        elif (player + pc) % 2 != 0:
            print(f'O computador jogou {pc} e vc jogou {player}')
            print('\033[1;31mVOCE PERDEU!!!!\033[m')
            print('--' * 12)
            break

    if jog in 'Ii':

        if (player + pc) % 2 == 0:
            print(f'O computador jogou {pc} e vc jogou {player}')
            print('\033[1;31mVOCE PERDEU!!!!\033[m')
            print('--' * 12)
            break

        elif (player + pc) % 2 != 0:
            print(f'O computador jogou {pc} e vc jogou {player}')
            print('\033[1;32mVOCE GANHOU!!!!\033[m')
            cont += 1

print('GAME OVER')
print(f'Voce ganhou um total de {cont} vezes')
