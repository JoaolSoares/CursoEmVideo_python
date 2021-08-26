from time import sleep
opc = 0

n1 = float(input('Digite o 1º numero: '))
n2 = float(input('Digite o 2º numero: '))
print('--' * 15)

while opc != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Dizer qual é o maior
[ 4 ] Digitar novamente
[ 5 ] Sair do programa''')
    print('--' * 15)

    opc = int(input('Digite a opção escolhida: '))

    if opc == 1:
        print('A soma entre {} e {} é: {}' .format(n1, n2, n1 + n2))

    if opc == 2:
        print('A multiplicaçao entre {} e {} é: {}' .format(n1, n2, n1 * n2))

    if opc == 3:
        if n1 > n2:
            print('O maior numero é o {}' .format(n1))
        if n1 < n2:
            print('O maior numero é o {}'.format(n2))

    if opc == 4:
        print('Reiniciando...')
        sleep(1)
        print('--' * 20)
        n1 = float(input('Digite o 1º numero: '))
        n2 = float(input('Digite o 2º numero: '))

    if opc > 5:
        print('Opão invalida, tente novamente...')

    print('--' * 20)

print('Finalizando...')
sleep(1)
print('Programa finalizado')
