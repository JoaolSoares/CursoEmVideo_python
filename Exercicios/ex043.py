peso = float(input('Diga o seu peso atual: (Kg) '))
altura = float(input('Diga a sua altura atual: (m) '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('\033[1;31mABAIXO DO PESO')

if 18.5 <= imc <= 25:
    print('\033[1;32mPESO IDEAL')

if 25 < imc <= 30:
    print('\033[1;33mSOBREPESO')

if 30 < imc <= 40:
    print('\033[1;31mOBESIDADE')

if 40 < imc:
    print('\033[1;30;41mOBESIDADE MORBIDA\033[m')
