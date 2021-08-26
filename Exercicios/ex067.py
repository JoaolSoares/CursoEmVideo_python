from time import sleep

print('\033[1;34m-\033[m' * 30)
print('\033[1;32m{:-^30}\033[m' .format(' CALCULADOR DE TABUADA '))
print('\033[1;34m-\033[m' * 30)
print('')

cont = 11
t = 0
while True:
    if cont == 11:
        t = int(input('Digite o numero para saber sua TABUDA [0 para finalizar]: '))
        cont = 0

        if t == 0:
            break

    while True:     # com o for ficaria melhor, mas eu fiz com while por que a aula é sobre isto
                    # eu até pensei em fazer com o for, mas, quis me desafiar usando apenas coisas da aula
        if t == 0:
            break

        cont += 1

        if cont <= 10:
            print(f'{cont} X {t} = {cont * t}')

        if cont == 11:
            print('-=' * 20)
            break

print('Finalizando', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.')
sleep(0.5)
print('Programa finalizado com sucesso, volte sempre :D')
