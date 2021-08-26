n1 = float(input('Digite um numero para ver sua tabuada: '))
n2 = int(input('Até que onde quer sua tabuada? '))
for t in range(1, n2 + 1):
    print('{} X {} = {}' .format(t, n1, t * n1))
