mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacol = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        mat[l][c] = int(input(f'Digite o numero referentre a [{l},{c}] da matriz: '))

        if mat[l][c] % 2 == 0:
            somapar += mat[l][c]

        if c == 2:
            somacol += mat[l][c]

        if l == 1:
            if c == 0:
                maior = mat[l][c]
            if mat[l][c] > maior:
                maior = mat[l][c]

print('-=' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{mat[l][c]:^5}]', end='')
    print()

print('-=' * 20)
print(f'A soma de todos os elementos pares é: {somapar}')
print(f'A soma de todos os valores da terceira coluna é: {somacol}')
print(f'O maior numero da segunda linha é {maior}')
