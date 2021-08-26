print('--' * 12)
print('----- Banco do jão -----')
print('--' * 12)
print('')

saca = int(input('Quanto deseja sacar? R$'))
total = saca
ced = 200
totalc = 0

while True:
    if total >= ced:
        total -= ced
        totalc += 1

    else:
        if totalc != 0 and ced > 10:
            print(f'{totalc} cedulas de R${ced} reais.')

        elif ced < 10:
            print(f'{totalc} moedas de R${ced} reais.')

        if ced == 200:
            ced = 100
            totalc = 0

        elif ced == 100:
            ced = 50
            totalc = 0

        elif ced == 50:
            ced = 20
            totalc = 0

        elif ced == 20:
            ced = 10
            totalc = 0

        elif ced == 10:
            ced = 1
            totalc = 0

        elif ced == 1:
            ced = 0
            totalc = 0

        elif ced == 0:
            break
