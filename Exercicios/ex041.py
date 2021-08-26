from datetime import date

ano = date.today().year
nasc = int(input('Diga o seu ano de nascimento: '))
print('=' * 30)

if ano - nasc <= 9:
    print(' Voce possui \033[1;34m{} anos\033[m, e sua categoria é \033[1;32mMIRIM' .format(ano - nasc))

elif 9 < ano - nasc <= 14:
    print(' Voce possui \033[1;34m{} anos\033[m, e sua categoria é \033[1;32mINFANTIL' .format(ano - nasc))

elif 14 < ano - nasc <= 19:
    print(' Voce possui \033[1;34m{} anos\033[m, e sua categoria é \033[1;32mJUNIOR' .format(ano - nasc))

elif 19 < ano - nasc <= 20:
    print(' Voce possui \033[1;34m{} anos\033[m, e sua categoria é \033[1;32mSÊNIOR' .format(ano - nasc))

else:
    print(' Voce possui \033[1;34m{} anos\033[m, e sua categoria é \033[1;32mMASTER'.format(ano - nasc))
