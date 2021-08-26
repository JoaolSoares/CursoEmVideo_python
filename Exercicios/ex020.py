from random import shuffle
a1 = input('Diga o nome de um aluno: ')
a2 = input('Diga o nome de um aluno: ')
a3 = input('Diga o nome de um aluno: ')
a4 = input('Diga o nome de um aluno: ')

lista = [a1, a2, a3, a4]
shuffle(lista)

print('')
print('{:-^70}' .format(''))
print('A ordem escolhida foi: {}' .format(lista))
print('{:-^70}' .format(''))
