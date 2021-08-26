r = 's'
id18cont = mcont = f20cont = 0

# Esta sem a validação de dados...

while True:
    print('--' * 15)
    print('Cadastro de pessoas')
    print('--' * 15)

    idade = int(input('Qual a idade? '))
    sex = str(input('Qual o sexo? [M/F] ')).strip().upper()[0]
    print('--' * 15)
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if idade > 18:
        id18cont += 1

    if sex in 'Mm':
        mcont += 1

    elif sex in 'Ff' and idade < 20:
        f20cont += 1

    if r in 'Nn':
        break

print(f'{id18cont} pessoas tem mais de 18 anos')
print(f'{mcont} Homens foram cadastrados')
print(f'{f20cont} Mulheres com menos de 20 anos foram cadastradas')
