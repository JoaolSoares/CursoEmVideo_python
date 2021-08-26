n1 = input('digite algo:')
print('o tipo primitivo desse valor é:', type(n1))
print('só tem espaços?', n1.isspace())
print('pode ser um numero?', n1.isnumeric())
print('é maiusulo?', n1.islower())
print('é minusculo?', n1.isupper())
print('é alfabetico?', n1.isalpha())
print('é alfanumerico?', n1.isalnum())
print('esta capitalizada(com maiusculas e minusculas)?', n1.istitle())
# Outra forma agora com a quebra de linha /n

n1 = input('digite algo')
s = type(n1)
p = n1.isspace()
n = n1.isnumeric()
print('primitive type {} \n só tem espaços? {} \n pode ser um numero? {}' .format(s , p , n))


