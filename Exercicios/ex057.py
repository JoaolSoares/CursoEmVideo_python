sex = 0                           # sex = input('Digite o seu sexo [M/F]: ').upper().strip()[0]
while sex != 'M' and sex != 'F':  # pode usar o while sex not in 'MmFf':
    sex = input('Digite o seu sexo [M/F]: ').upper().strip()[0] # só para pegar a primeira letra caso escreva 'Masculino'

    if sex != 'M' and sex != 'F':
        print('\033[1;31mSexo não valido, tente novamente\033[m')
        print('--' * 20)

print('\033[1;32mSexo "{}" computado com sucesso\033[1;32m' .format(sex))
