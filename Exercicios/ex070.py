print('--' * 15)
print('Loja Barracão do seu Claudio')
print('--' * 15)

soma = mil = menor = nmenor = cont = 0
r = 's'
while True:
    cont += 1
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: '))
    r = ' '

    while r not in 'SsNn':
        print('--' * 15)
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('--' * 15)

    soma += preco

    if preco > 999:
        mil += 1

    if cont == 1:
        menor = preco
        nmenor = nome

    if cont > 1:
        if preco < menor:
            menor = preco
            nmenor = nome

    if r in 'Nn':
        break

print('-------- FIM DO PROGRAMA --------')
print(f"""Total da compra: {soma}
Itens Com valor mais alto que mil reais: {mil}
O produto mais barato foi {nmenor} custando {menor}""")
