lista = []
maior = menor = 0

for n in range(0, 5):
    lista.append(int(input('Digite um numero: ')))

    if n == 0:
        maior = menor = lista[n]

    else:

        if lista[n] > maior:
            maior = lista[n]

        if lista[n] < menor:
            menor = lista[n]

print('-' * 40)
print(f'A lista foi -> {lista}')
print('-' * 40)

print(f'O maior valor digitado foi o {maior} na posição ', end='')

for c, v in enumerate(lista):
    if v == maior:
        print(c, end=' ')

print(f'\nO menor valor digitado foi o {menor} na posição ', end='')

for c, v in enumerate(lista):
    if v == menor:
        print(c, end=' ')
