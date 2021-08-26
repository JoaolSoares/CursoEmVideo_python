media = 0
hvelho = 0
idadevelho = 0
mcont = 0
for c in range(1, 5):
    nome = str(input('Qual o nome da {}ª pessoa? ' .format(c))).strip()
    idade = int(input('Qual a idade da {}ª pessoa? ' .format(c)))
    sexo = str(input('Qual o sexo da {}ª pessoa? use:(M,F):  ' .format(c))).upper().strip()
    print('--' * 13)

    media += idade
    # if c == 1 and sexo in 'Mm':
    if sexo == 'M':
        if c == 1:
            hvelho = nome
            idadevelho = idade

        else:
            if idade > idadevelho:
                idadevelho = idade
                hvelho = nome

    elif sexo == 'F':
        if idade < 20:
            mcont += 1

print('A media de idade das 5 pessoas é {}' .format(media / 4))
print('O HOMEM mais velho é o {} com {} anos' .format(hvelho, idadevelho))
print('Existem {} MULHERES com menos de 20 anos' .format(mcont))
