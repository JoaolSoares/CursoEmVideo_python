num = float(input('Digite um numero: '))
cont = 1
maior = menor = num
soma = num
r = 's'

while r in 'Ss':
    n1 = float(input('Digite mais um numero: '))
    r = str(input('Voce que continuar? (S/N): '))[0].strip()
    soma += n1

    if n1 > maior:
        maior = n1

    if n1 < menor:
        menor = n1

    cont += 1

print('-' * 20)
print('Voce digitou {} numeros, a MEDIA entre eles é {}' .format(cont, soma / cont))
print('O MAIOR valor foi {} e o MENOR foi {}' .format(maior, menor))
