from datetime import date
ano = date.today().year
nasc = int(input('Diga o seu ano de nascimento: '))

print('\033[1;34m=\033[m' * 50)
print('Voce possui {} anos' .format(ano - nasc))
print('\033[1;34m=\033[m' * 50)

if nasc > ano - 18:
    print('Você ainda não precisa se alistar.')
    print('-' * 50)
    print('\033[1;33mVoce devera se alistar em {}\033[m' .format(nasc + 18))

elif nasc == ano - 18:
    print('\033[1;32mVocê precisa se alistar este ano.\033[m')

elif nasc < ano - 18:
    print('Você já se alistou OU deveria ter se alistado.')
    print('-' * 50)
    print('\033[1;31mVoce deveria ter se alistado em {}\033[m'.format(nasc + 18))
