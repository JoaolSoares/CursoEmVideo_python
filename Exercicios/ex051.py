print('-' * 5, 'Leitor de P.A', 5 * '-')

pt = int(input('Diga o primeiro termo da P.A: '))
# ut = int(input('Diga até onde essa P.A vai: '))
rz = int(input('Diga a razão dessa P.A: '))
n1 = 10 * rz

for pa in range(pt, pt + 10 * rz, rz):
    print(pa, end=' -> ')

print('Acabou')
