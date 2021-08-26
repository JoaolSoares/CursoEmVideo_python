d1 = float(input('Diga o desconto aplicado: '))
p1 = float(input('Diga o preço do produto: '))
desconto = (p1 * d1) / 100
print('O preço do produto com {}% de descondo ficará: {:.2f}' .format(d1 , p1 - desconto))
