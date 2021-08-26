from random import randint

pc = randint(1, 10)

print('Eu pensei em um numero entre 1 e 10, tente adivinha-lo se for capaz...')
n1 = int(input('Digite aqui a sua tentativa: '))

tent = 1
while n1 != pc:
    print('--' * 20)
    print('\033[1;31mVoce errou, mas, pode tentar novamente...\033[m')
    n1 = int(input('Digite aqui a sua outra tentativa: '))
    tent += 1

if tent == 0:
    print('--' * 20)
    print('\033[1;32mVoce acertou de primeira!!!\033[m')

else:
    print('--' * 20)
    print('\033[1;35mVoce acertou, mas, precisou tentar {} vezes... patetico\033[m' .format(tent))
