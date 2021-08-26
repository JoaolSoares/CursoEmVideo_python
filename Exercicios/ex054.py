from datetime import date
cont = 0
cont2 = 0
for c in range(1, 8):
    nasc = int(input('Qual o ano de nascimento da {}º pessoa? ' .format(c)))
    if date.today().year - nasc >= 18:
        cont += 1
    else:
        cont2 += 1
print('--' * 20)
print('Existem {} pessoas MAIORES de idade.\nExistem {} pessoas MENORES de idade.' .format(cont, cont2))
