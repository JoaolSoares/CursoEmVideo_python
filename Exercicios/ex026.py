frase = str(input('Digite uma frase: ')).lower()
print('A letra "a" aparece {} vezes na sua frase' .format(frase.count('a')))
print('A letra "a" aparece sua primeira vez no caracter: {}' .format(frase.find('a') + 1))
print('A letra "a" aparece sua ultima vez no caracter: {}' .format(frase.rfind('a') + 1))
