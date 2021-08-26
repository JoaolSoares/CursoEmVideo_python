from random import choice
from time import sleep
lista = ['Pedra', 'Papel', 'Tesoura']
pc = choice(lista)
# poderia fazer tambem com:
# listaa = ('Pedra', 'Papel', 'Tesoura')
# pcc = randint(1, 3)
# print('O computador escolheu {}' .format(lista[pcc]))
# metodo menos eficiente (eu acho) ^
print('\033[1;34m-\033[m' * 3, '\033[1;32mJOKENPO\033[m', '\033[1;34m-\033[m' * 3)

print('')
print('\033[1;36m-\033[m' * 25)
print('[ 1 ] Pedra')
print('[ 2 ] Papel')
print('[ 3 ] Tesoura')
print('\033[1;36m-\033[m' * 25)

esc = (input('Diga a sua escolha: ')).strip()
print('\033[1;36m-\033[m' * 25)

if esc == '1' or esc == '2' or esc == '3':                              # numeros dentro da lista
    if esc == '1':
        esc = 'Pedra'
    elif esc == '2':
        esc = 'Papel'
    elif esc == '3':
        esc = 'Tesoura'

    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO')
    sleep(0.5)
    print('\033[1;36m-\033[m' * 25)

    if esc == 'Pedra' and pc == 'Tesoura' or esc == 'Papel' and pc == 'Pedra' or esc == 'Tesoura' and pc == 'Papel':
        print('Sua escolha: {}'.format(esc))                                     # vitoria
        print('Escolha do computador: {}'.format(pc))
        print('\033[1;32mPARABENS!!! Voce ganhou!\033[m')

    elif esc == pc:                                                              # empate
        print('Sua escolha: {}'.format(esc))
        print('Escolha do computador: {}'.format(pc))
        print('\033[1;34mEMPATOU!\033[m')

    elif pc == 'Pedra' and esc == 'Tesoura' or pc == 'Papel' and esc == 'Pedra' or pc == 'Tesoura' and esc == 'Papel':
        print('Sua escolha: {}' .format(esc))                                    # derrota
        print('Escolha do computador: {}' .format(pc))
        print('\033[1;31mNÃO FOI DESSA VEZ! Você perdeu\033[m')

else:                                                                            # numeros fora da lista ou letras
    print('\033[1;31mErro')
