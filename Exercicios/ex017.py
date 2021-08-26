ca = float(input('Diga o cateto adjacente do triangulo retangulo: '))
co = float(input('Diga o cateto oposto do triangulo retangulo: '))
h = (ca ** 2 + co ** 2) ** (1/2)
#Da pra usar a formula
#h2 = ca ** 2 + co ** 2
#h = h2 ** (1 / 2)
print('O valor da hipotenusa do triangulo retangulo é: {:.3f}' .format(h))

print(' ')
print('{:-^25}' .format(''))
print('agora com o math inportado')
print('{:-^25}' .format(''))
print(' ')

from math import hypot
ca = float(input('Diga o cateto adjacente do triangulo retangulo: '))
co = float(input('Diga o cateto oposto do triangulo retangulo: '))
h = hypot(ca , co)
print('O valor da hipotenusa do triangulo retangulo é: {:.3f}' .format(h))
