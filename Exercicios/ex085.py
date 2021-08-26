lista = [[], []]
for c in range(1, 8):
    n1 = int(input(f'Digite o {c}º Numero: '))

    if n1 % 2 == 0:
        lista[0].append(n1)
    else:
        lista[1].append(n1)

print('\033[1;35m-+\033[m' * 18)
print(f'Numeros pares: {sorted(lista[0])}')
print(f'Numeros impares: {sorted(lista[1])}')
