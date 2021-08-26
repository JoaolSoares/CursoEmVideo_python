def criararq(nome='', idade=0):
    global lista
    arq = open("dados.txt", "a+")

    arq.write(f'{nome}\n')
    arq.write(f'{idade}\n')

    arq.close()


def leituraarq(arquivo):

    arq = open(arquivo, "r")
    arqstring = arq.readlines()

    arq.close()

    return arqstring


def idadevalid():
    while True:
        try:
            idade = int(input('IDADE: '))
        except(ValueError, KeyboardInterrupt):
            print('\033[1;31mERRO! O valor digitado não é valido, tente novamente...\033[m')
            print('-' * 10)
            continue
        else:
            break
    return idade
