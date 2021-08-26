from time import sleep
from interface import modinterface
from arquivo import modaarquivo


while True:
    opc = modinterface.menu('MENU PRINCIPAL',
                            'Ver pessoas cadastradas',
                            'Cadastrar pessoa nova',
                            'Sair',
                            'Limpar Cadastros')

    modinterface.menusec(opc)

    if opc == 1:
        lista = modaarquivo.leituraarq('dados.txt')
        modinterface.tabela(lista)

        continue

    elif opc == 2:
        nome = str(input('NOME: ')).strip()
        idade = modaarquivo.idadevalid()
        modaarquivo.criararq(nome, idade)

        continue

    elif opc == 3:
        break

    elif opc == 4:
        arquivo = open('dados.txt', 'r+')
        arquivo.truncate(0)
        print('\033[1;32mCadastros limpos com sucesso\033[m')

sleep(0.3)
print('\033[1;31m   -Finalizando o programa', end='')
sleep(0.5)
print(end=' .')
sleep(0.5)
print(end=' .')
sleep(0.5)
print(' .\033[m')
sleep(0.3)
print('\033[1;32m   -Programa finalizado com sucesso, volte sempre ;D\033[m')
