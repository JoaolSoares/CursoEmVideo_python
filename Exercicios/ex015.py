d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km o carro rodou? '))
p1 = d * 60
p2 = km * 0.15
print('O aluguel cobrado pelo carro será: {:.2f}' .format(p1 + p2))
print('{:-^42}' .format(''))
