num = float(input('Digite um numero: '))

cont = n1 = 0
soma = num

while n1 != 999:
    soma += n1
    cont += 1
    n1 = float(input('Digite mais um numero (999 para parar): '))

print('Voce digitou {} numeros e a soma deles é {}' .format(cont, soma))
