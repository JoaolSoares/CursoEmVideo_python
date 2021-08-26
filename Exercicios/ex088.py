from random import randint

lista = []
jogos = []

n1 = int(input('Quantos jogos você quer? '))

for c in range(0, n1):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.append(sorted(lista[:]))
    lista.clear()

for j in jogos:
    print(j)
