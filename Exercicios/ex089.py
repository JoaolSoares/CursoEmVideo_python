aluno = []
lista = []
res = 'S'

print('\033[1;35m--' * 15)
print(f'{"Sistema Do Colegio":^30}')
print('--' * 15, '\033[m')
print('----')

# Coleta de dados
while res in 'Ss':
    aluno.append(str((input('Nome do aluno: '))))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    aluno.append((aluno[1] + aluno[2]) / 2)
    lista.append(aluno[:])
    aluno.clear()
    res = str(input('Quer continuar? [S/N] '))
    print('-=' * 25)

# Tabela
print('\033[1;35mNº  ALUNO        NOTA')
print('-' * 25, '\033[m')
for c, a in enumerate(lista):
    print(f'{c}   {a[0]:<12} {a[3]}')
print('\033[1;35m-' * 25, '\033[m')

# Notas separadas dos alunos
while res != 999:
    res = int(input('Nº do aluno para saber sua nota separada [999 para finalizar]: '))

    if res > (len(lista) - 1) and res != 999:
        print('\033[1;31mNão encontrei este aluno... Tente novamente...\033[m')
    elif res != 999:
        print(f'As notas do aluno {lista[res][0]} foram {lista[res][1]} e {lista[res][2]}...')

    print('-=' * 25)

print('Programa Finalizado com sucesso...')
