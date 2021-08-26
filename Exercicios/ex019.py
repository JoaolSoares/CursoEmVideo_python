from random import choice
a1 = input('Diga o nome de um aluno')
a2 = input('Diga o nome de um aluno')
a3 = input('Diga o nome de um aluno')
a4 = input('Diga o nome de um aluno')

lista = [a1, a2, a3, a4]

print('{:-^30}' .format(''))
print('O aluno escolhido foi: {}' .format(choice(lista)))
print('{:-^30}' .format(''))
