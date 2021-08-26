nums = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
        'treze', 'quatorze', 'quize', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

n1 = int(input('Diga um numero entre 0 e 20 [999 para finalizar]: '))

while True:
    if n1 != 999:

        while 0 <= n1 <= 20:
            print(f'O numero escolhedo foi o {nums[n1]}')
            print('--' * 20)
            n1 = int(input('Diga um numero entre 0 e 20 [999 para finalizar]: '))

        while not 0 <= n1 <= 20 and n1 != 999:
            print('Erro...')
            n1 = int(input('Por favor, Diga um numero entre 0 e 20 [999 para finalizar]: '))

    if n1 == 999:
        print('--' * 20)
        break

print('O programa foi finalizado com sucesso...')
