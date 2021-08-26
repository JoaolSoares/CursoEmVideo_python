import random
n = random.randint(0, 5)
print('-=' * 33)
n2 = int(input('Eu acabei de pensar em um numero entre 0 e 5, tente adivinha-lo...\n Digite aqui: '))
print('-=' * 33)
if n2 == n:
    print('PARABÉNS! Voce acertou o numero escolhido por mim!!!!!')
else:
    print('NAO FOI DESSA VEZ! Hahaha! Tente da proxima...')
