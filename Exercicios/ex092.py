from datetime import datetime

dados = dict()

dados['nome'] = str(input('Nome: '))
dados['idade'] = datetime.now().year - int(input('Ano de Nascimento: '))
dados['CTPS'] = int(input('Nº CTPS [0 = inexistente]: '))

if dados['CTPS'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: '))
    contribuicao = (datetime.now().year - dados['contratacao'])
    dados['aposentedaria'] = dados['idade'] + (35 - contribuicao)

print('-=' * 20)
for k, v in dados.items():
    print(f'- {k} é {v}')
