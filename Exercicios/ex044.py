print('\033[1;34m-\033[m' * 10, '\033[1;32mLOJA\033[m', '\033[1;34m-\033[m' * 10)

valor = float(input('Digite o valor a ser pago: R$ '))

print('')
print('\033[1;34m-\033[m' * 55)
print('[ 1 ] Dinheiro / Cheque (10% de desconto)')
print('[ 2 ] Cartão (5% de desconto)')
print('[ 3 ] Parcelado 2x no cartão (sem juros)')
print('[ 4 ] Parcelado 3x ou mais no cartã0 (20% de juros)')
print('\033[1;34m-\033[m' * 55)
print('')

esc = int(input('Digite o metodo de pagamento: '))


print('\033[1;34m-\033[m' * 55)

if esc == 1:
    desc = (valor * 10) / 100
    print('\033[1;32mO valor a ser pago é de R$ {:.2f}\033[1;33m' .format(valor - desc))

elif esc == 2:
    desc = (valor * 5) / 100
    print('\033[1;32mO valor a ser pago é de R$ {:.2f}\033[1m'.format(valor - desc))

elif esc == 3:

    print('\033[1;32mA parcela mensal a ser paga é de 2x R$ {:.2f}\033[1m'.format(valor / 2))

elif esc == 4:
    print('')
    parcela = int(input('Digite o numero de parcelas desejadas: '))
    juros = (valor * 20) / 100
    print('')
    print('\033[1;34m-\033[m' * 55)
    if parcela >= 3:
        print('\033[1;32mA parcela mensal a ser paga é de {}x R$ {:.2f}\033[1m'.format(parcela,
                                                                                       (valor + juros) / parcela))
        print('')
    else:
        print('\033[1;31mO valor de parcelas selecionado não é valido,'
              'tente novamente.\033[1m')


else:
    print('\033[1;31mErro... tente  novamente.')

print('\033[1;34m-\033[m' * 55)
