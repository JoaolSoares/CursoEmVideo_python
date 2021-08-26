print('-' * 9)
print('Fibonacci')
print('-' * 9)

n = int(input('Digite quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
cont = 3

if n == 1:
    print(t1, end='')

else:
    print('{} -> {}' .format(t1, t2), end='')

    while cont <= n:
        t3 = t1 + t2
        print(' -> {}' .format(t3), end='')
        cont += 1
        t1 = t2
        t2 = t3


print(' -> Fim')
