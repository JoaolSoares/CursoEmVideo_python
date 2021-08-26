soma = 0
for c in range(1, 7):
    n1 = int(input('Diga um {}º numero: ' .format(c)))
    if n1 % 2 == 0:
        soma += n1
print('A soma de todos os numeros pares é de: \033[1;34m{}\033[m'. format(soma))
