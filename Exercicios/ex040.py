n1 = float(input('Diga a primeira nota: '))
n2 = float(input('Diga a sua segunda nota: '))

print('')
print('=' * 20)
media = (n1 + n2) / 2
print('A sua media foi {}'.format(media))
print('=' * 20)

if media < 5.0:
    print('\033[1;31mREPROVADO!')

elif media >= 5 and media <= 6.9:
    print('\033[1;33mRECUPERAÇÃO!')

else:
    print('\033[1;32mAPROVADO!')
