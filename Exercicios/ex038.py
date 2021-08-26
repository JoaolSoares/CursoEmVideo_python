n1 = int(input('Digite um primeiro valor: '))
n2 = int(input('Digite um segundo valor: '))
print('--' * 12)
if n1 < n2:
    print('O segundo valor é MAIOR')
elif n2 < n1:
    print('O primeiro valor é MAIOR')
else:
    print('os dois valores são IGUAIS')
