from time import sleep

lista = [int(input('Digite um valor: '))]
print('\033[1:32mValor adicionado com sucesso!\033[m')

while True:
    res = input('Quer continuar? [S/N] ')[0].upper()
    print('-' * 30)

    if res == 'S':
        n1 = int(input('Digite um valor: '))

        if lista.count(n1) == 0: #Ou poderia usar    if n1 not in lista:
            lista.append(n1)
            print('\033[1:32mValor adicionado com sucesso!\033[m')

        else:
            print('\033[1:31mValor repitido, não foi adicionado a lista\033[m')

    if res == 'N':
        break

print('\033[1:36mCalculando...\033[m')
print('-' * 30)
sleep(1)

print(f'A lista em ordem crescente foi {sorted(lista)}')
