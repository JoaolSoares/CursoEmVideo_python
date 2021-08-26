from utilidadesCEV import moeda
from utilidadesCEV import dados

num = dados.leiadinheiro()
p_aument = int(input('Taxa a ser adicionado: '))
p_desct = int(input('Taxa a ser descontada: '))

moeda.resumo(num, p_aument, p_desct)
