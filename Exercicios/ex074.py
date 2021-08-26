import random

n1 = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100),
      random.randint(0, 100), random.randint(0, 100))

print('\033[1;34mNumeros selecionados pelo computador:\033[m')

for n in n1:
    print(n, end=' ')

print('\n', end='')
print('\033[1;34m--\033[m' * 17)

print(f'O maior valor foi {max(n1)}')
print(f'O menor valor foi {min(n1)}')
