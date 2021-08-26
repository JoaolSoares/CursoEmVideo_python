n1 = int(input('Digite um numero: ').strip())
print('{:-^20}' .format(''))
print('O numero possui: ')

print('Milhar: {}' .format(n1 // 1000 % 10))
print('Centena: {}' .format(n1 // 100 % 10))
print('Dezena: {}' .format(n1 // 10 % 10))
print('Unidade: {}' .format(n1 // 1 % 10))

print('{:-^20}' .format(''))
