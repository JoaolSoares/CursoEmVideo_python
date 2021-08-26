def voto(ano):
    from datetime import date

    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: \nVoto Negado'
    elif 65 > idade >= 18:
        return f'Com {idade} anos: \nVoto Obrigatorio'
    else:
        return f'Com {idade} anos: \nVoto opcional'


votado = voto(int(input('Ano de nascimento: ')))
print('-=' * 20)
print(f'{votado}')
