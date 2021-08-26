t1 = (int(input('Digite um numero: ')), int((input('Digite mais um numero: '))),
      int(input('Digite um numero: ')), int(input('Digite um ultimo numero: ')))

print('--' * 15)
print(f'Os Valores digitados foram {t1}')

print('--' * 15)
if t1.count(9) >= 1:
    print(f'O numero 9 foi digitado {t1.count(9)} vezes')

elif t1.count(9) == 0:
    print(f'O numero 9 foi digitado nenhuma vez')

if t1.count(3) >= 1:
    print(f'O numero 3 apareceu pela primeira vez na {t1.index(3) + 1}ª posição')

elif t1.count(3) == 0:
    print(f'O numero 3 não apareceu nenhuma vez')

print(f'Numero pares digitados:', end=' ')

if t1[0] % 2 == 0:
    print(t1[0], end=' ')
if t1[1] % 2 == 0:
    print(t1[1], end=' ')
if t1[2] % 2 == 0:
    print(t1[2], end=' ')
if t1[3] % 2 == 0:
    print(t1[3], end=' ')

#Poderia fazer tambem:
#for c in t1:
#    if c % 2 == 0:
#        print(c, end=' ')