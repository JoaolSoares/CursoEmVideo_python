from math import(pi , cos , sin , tan , radians)

an1 = float(input('Diga o angulo: '))
an2 = (an1 * pi) / 180
# Podemos usar tambem o math: an2 = radians(an1)
# sen = (sin(radians(an1)))
sen = sin(an2)
cos = cos(an2)
tg = tan(an2)

print('')
print('{:-^30}' .format(''))
print('O SENO do angulo {} é: {:.3f}' .format(an1 , sen))
print('O COSSENO do angulo {} é: {:.3f}' .format(an1 , cos))
print('A TANGENTE do angulo {} é: {:.3f}' .format(an1 , tg))
print('{:-^30}' .format(''))
