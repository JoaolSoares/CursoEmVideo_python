n1 = str(input('Digite o seu nome inteiro: ')).strip()
print('{:-^60}' .format(''))
print('O seu nome com letras maiusculas fica: {}' .format(n1.upper()))
print('O seu nome com letras minusculas fica: {}' .format(n1.lower()))
print('O seu nome tem {} letras no total' .format(len(n1) - n1.count(' ')))
print('O seu primeiro nome é {} tem {} letras' .format((n1.split())[0], len((n1.split())[0])))
#print('O seu primeiro nome tem {} letras' .format(n1.find(' '))) <--- maneira mais simples porem menos complexa
print('{:-^60}' .format(''))
