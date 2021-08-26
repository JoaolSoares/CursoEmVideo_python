n1 = float(input('Diga quantos KM tem a sua viagem: '))
if n1 <= 200:
    print('O preço da sua passagem ficara R${}' .format(n1 * 0.50))
else:
    print('O preço da sua passagem ficara R${}' .format(n1 * 0.45))
print('Tenha uma boa viagem!! ;D')