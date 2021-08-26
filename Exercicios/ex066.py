cont = soma = 0
while True:
    num = float(input('Digite um numero (999 para parar): '))

    if num == 999:
        break

    soma += num
    cont += 1

print(f'Voce digitou {cont} numeros e a soma deles é {soma}')
