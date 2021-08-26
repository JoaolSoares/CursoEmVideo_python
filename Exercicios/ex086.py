num = []
cont = 0
for c in range(1, 10):
    num.append(int(input('Digite um numero: ')))

print('-=' * 12)
for n in num:
    print(f'[{n:^5}]', end='')
    cont += 1
    if cont in (3, 6):
        print()


# no video ele faz de ioutra maneira:

num1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        num1[linha][coluna] = int(input(f'Digite o numero da posição [{linha},{coluna}]'))
