def leiaint(msg):
    while True:
        n1 = input(f'{msg} ')
        try:
            n1 = int(n1)
        except:
            if n1.strip() == '':
                n1 = 0
                print('\033[1;31m O usuario optou por não digitar este numero\033[m')
                break
            else:
                print('\033[1;31m ERRO, Tente novamente...\033[m')
                continue
        break
    return n1


def leiafloat(msg):
    while True:
        n1 = input(msg)

        try:
            n1 = float(n1)
        except:
            if n1.strip() == '':
                n1 = 0
                print('\033[1;31m O usuario optou por não digitar este numero\033[m')
                break
            else:
                print('\033[1;31m ERRO, Tente novamente...\033[m')
                continue
        break
    return n1


print('-=' * 20)
inteiro = leiaint('Digite um numero INTEIRO:')
real = leiafloat('Figite um numero REAL: ')
print('-=' * 20)
print(f' -O numero inteiro foi {inteiro} e o real foi {real}')
print('-=' * 20)
