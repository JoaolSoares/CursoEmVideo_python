lista = []

for c in range(0, 5):
    n1 = int(input('Digite um numero: '))

    if c == 0:
        print(f'O numero {n1} foi adicionado no começo da lista!')
        lista.append(n1)

    elif n1 > lista[len(lista) - 1]:
        lista.append(n1)
        print(f'O numero {n1} foi adicionado no final da lista!')

    else:
        cont = 0
        while cont < len(lista):
            if n1 <= lista[cont]:
                lista.insert(cont, n1)
                print(f'O numero {n1} foi adicionado na posi {cont} da lista!')
                break
            cont += 1

print('--' * 30)
print(lista)
