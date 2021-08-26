import moeda

num = float(input('Digite o preço R$ '))
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, f=True)}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, f=True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(num, 10, f=True)}')
print(f'Diminuindo 15%, temos {moeda.diminuir(num, 15, f=True)}')
