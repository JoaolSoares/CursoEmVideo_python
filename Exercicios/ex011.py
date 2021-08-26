alt = float(input('Qual a altura da parede? '))
larg = float(input('Qual a larguda da parede? '))
print('A area da sua parede é: {:.3f} metros quadrados' .format(alt * larg))
print('Para pintar a parede toda(considerando 1 litro de tinta para cada 2 metros quadrados), você precisara de {:.3f} litros de tinta' .format((alt * larg) / 2))


