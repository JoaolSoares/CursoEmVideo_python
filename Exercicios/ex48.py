soma = 0                 # <- acumulador
cont = 0                 # <- contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += + c      # <- soma = soma + c
        cont += + 1      # <- cont = cont + c
print('A soma de todos os {} valores é igual a {}' .format(cont, soma))
