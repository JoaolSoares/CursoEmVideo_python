n1 = int(input('Diga o primeiro numero:'))
n2 = int(input('Diga o segundo numero:'))
n3 = int(input('Diga o terceiro numero:'))
if n1 > n2 and n1 > n3:
    maior = n1
if n1 < n2 and n1 < n3:
    menor = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n2 < n1 and n2 < n3:
    menor = n2
if n3 > n1 and n3 > n1:
    maior = n3
if n3 < n1 and n3 < n2:
    menor = n3
print('O maior numero: {} \n O menor numero: {}' .format(maior, menor))
