def notas(*notas, sit=False):
    """
    -- Serve para analisar notas de alunos, e entregar dados em um dicionario
    :param notas: Todas as notas do aluno
    :param sit: a situacao dos alunos
    :return: um dicionario com total de notas adicionadas, media, e situação caso True
    """

    maior = menor = somanotas = 0
    turma = dict()
    turma['total'] = len(notas)

    for c, n in enumerate(notas):
        somanotas += n
        if c == 0:
            maior = menor = n
        else:
            if n > maior:                       # fui burro, podia usar só:
                maior = n                       # turma['maior'] = max(notas)
            if n < menor:                       # turma['menor'] = min(notas)
                menor = n                       # é uma Tupla ---------------

    turma['maior'] = maior
    turma['menor'] = menor

    turma['media'] = (somanotas / len(notas))   # Podia ter usado sum(notas)
                                                # Pois é uma tupla ---------
    if sit:
        if turma['media'] < 6:
            turma['situaçao'] = 'Ruim'
        elif 7 > turma['media'] >= 6:
            turma['situaçao'] = 'razoavel'
        else:
            turma['situaçao'] = 'Boa'

    return turma


print('-=' * 45)
print(notas(5.5, 9.5, 10, 6.5, sit=True))
print('-=' * 45)
help(notas)
