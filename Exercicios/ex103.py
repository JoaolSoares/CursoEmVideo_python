def ficha(nome='<Desconhecido>', gols=0):
    print(f'O jogador {nome} marcou {gols} gols no campeonato.')


n1 = input('Nome do jogador: ')
n2 = input('Gols no campeonato: ')
print('-=' * 20)

if n2.isnumeric():
    n2 = int(n2)
    if n1.strip() != '':
        ficha(n1, n2)
    else:
        ficha(gols=n2)

else:
    if n1.strip() != '':
        ficha(nome=n1)
    else:
        ficha()
