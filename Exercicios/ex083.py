ex = list(str(input('Digite uma expressõa matematica: ')))
lista = list()
for v in ex:
    if v in '(':
        lista.append('(')

    elif v in ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
# o cont += 1 e o cont -= 1
print('-+' * 20)

if len(lista) == 0:
    print('\033[1;32mA expressão esta correta!!\033[m')
else:
    print('\033[1;31mA expressão esta incorreta... :(\033[m')
