lista = list()
jogador = dict()
gols = list()
res = 'Ss'

while res in 'Ss':
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    total = 0
    for c in range(1, (jogador['partidas'] + 1)):
        numgol = int(input(f'Gols na {c}º partida: '))
        gols.append(numgol)
        total += numgol

    jogador['gols'] = gols[:]
    jogador['total'] = total
    gols.clear()

    lista.append(jogador.copy())

    res = str(input('Quer continuar? [S/N] ')).upper()[0]

print()
print('-=' * 19)
print('Nº  Jogador       Gols         Total')
print('-=' * 19)
for c, v in enumerate(lista):
    print(f'{c + 1}   {v["nome"]:<14} {v["gols"]}     {v["total"]}')
print('-=' * 19)

res2 = 0
while res2 != 999:
    print('-=' * 19)
    res2 = int(input('Digite o numero de um jogador para saber seus gols [999 para finalizar] '))

    if res2 > (len(lista) + 1) and res2 != 999:
        print('Não encontrei nenhum jogador com este numero...')

    elif res2 != 999:
        print(f'-=' * 19)
        print(f'Gols do {lista[res2 - 1]["nome"]}')

        for c, v in enumerate(lista[res2 - 1]["gols"]):
            print(f' -Na partida {c + 1}: {v} gols')

    else:
        break

print('   -- Programa finalizado com sucesso --  ')
