lista = list()
res = 'S'
while True:
    if res in 'S':
        lista.append(int(input('Digite um numero: ')))
        res = str(input('Quer continuar? [S/N] ')).upper()[0]

    if res in 'N':
        break

print('--' * 20)

print(f'Foram digitados {len(lista)} valores...')
lista.sort(reverse=True)
print(f'A lista em forma decrescente foi: {lista}')

if 5 in lista:
    print(f'O valor 5 esta na lista')
else:
    print(f'O valor 5 não esta na lista')
