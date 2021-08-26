aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('Media do aluno: '))

if aluno['media'] >= 7:
    aluno['situacao'] = '\033[4;32mAprovado\033[m'
elif aluno['media'] < 7:
    aluno['situacao'] = '\033[4;31 mRecuperação\033[m'

print('-=' * 15)
for k, v in aluno.items():
    print(f'{k} é {v}')
