import moeda

num = float(input('Digite o preço R$ '))
p_aument = int(input('Taxa a ser adicionado: '))
p_desct = int(input('Taxa a ser descontada: '))

moeda.resumo(num, p_aument, p_desct)
