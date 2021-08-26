pes = []
tot = []
mai = men = cont = 0
res = 'S'
while True:
    if res in 'Ss':
        pes.append(str(input('Nome: ')))
        pes.append(float(input('Peso: ')))
        res = str(input('Quer continuar? [S/N] ')).upper()[0]
        tot.append(pes[:])
        if cont == 0:
            mai = men = pes[1]
        else:
            if pes[1] > mai:
                mai = pes[1]
            if pes[1] < men:
                men = pes[1]

        cont += 1
        pes.clear()

    else:
        break

print('-+' * 20)
print(f'Voce cadastrou {len(tot)} de pessoas no total!')

print(f'O maior peso lido foi {mai}Kg, pertencentes a: ', end='')
for p in tot:
    if p[1] == mai:
        print(p[0], end=' ')

print()
print(f'O menor peso lido foi {men}Kg, pertencentes a: ', end='')
for p in tot:
    if p[1] == men:
        print(p[0], end=' ')
