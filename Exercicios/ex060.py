n1 = int(input('Digite um numero para saber seu fatorial: '))
fat = 1

for c in range(n1, 0, -1):
    fat = fat * c
print('O valor de {}! é {} ' .format(n1, fat))
#
#
#
#
#

n2 = int(input('Digite um numero para saber seu fatorial: '))
c = n2
f = 1
while c > 0:

    f *= c
    c -= 1
print(f)

