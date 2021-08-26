lista = []
listapar = []
listaimpar = []
while True:
    n1 = int(input('Digite um numero: '))
    res = str(input('Quer continuar? [S/N] ')).upper()[0]
    lista.append(n1)

    if n1 % 2 == 0:
        listapar.append(n1)
    else:
        listaimpar.append(n1)

    if res in 'Nn':
        break
print('-+' * 20)

print(f'Lista completa: {lista}')
print(f'Numero pares: {listapar}')
print(f'Numeros impares: {listaimpar}')

# poderia utilizar o enumerate no final.
