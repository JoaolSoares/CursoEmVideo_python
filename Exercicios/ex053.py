frase = str(input('Digite umas frase: ').replace(' ', '')).lower()

#frasesemespaço = ''.join(frase.split())
# inverso = ''
# for c in range(len(frase) - 1, -1, -1):
#    inverso += frase[c]
# print(inverso)

contrario = frase[:: -1]
print('a frase ao contrario fica {}' .format(contrario))
if contrario == frase:
    print('é um polimedro')
else:
    print('Nao é um polimedro')