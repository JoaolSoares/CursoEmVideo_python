res = 'S'
lista = []

while True:
    if res in 'Ss':
        n1 = int(input('Digite um numero: '))

        if n1 in lista:
            print('\033[1;31mO numero digitado já esta na lista, não adicionado...\033[m')

        if n1 not in lista:
            print('\033[1;32mNumero adicionado a lista com sucesso!\033[m')
            lista.append(n1)

        res = str(input('Voce quer continuar? [S/N]: '))[0].upper()

    if res in 'Nn':
        break

    print('--' * 20)

print('\033[1;34m+-\033[m' * 30)
print(f'A lista digitada em forma crescente foi: {sorted(lista)}')
