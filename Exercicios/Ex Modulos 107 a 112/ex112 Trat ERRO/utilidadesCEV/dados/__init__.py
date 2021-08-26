def leiadinheiro():

    while True:
        n = str(input('Digite um PREÇO: R$ ')).strip().replace(',', '.')

        if n.isalpha() or len(n) == 0:
            print(f'\033[1;31mERRO! \"{n}\" é um valor invalido, tente novamente...\033[m')
        else:
            try:
                n = float(n)
            except:
                print(f'\033[1;31mERRO! \"{n}\" é um valor invalido, tente novamente...\033[m')
            else:
                n = float(n)
                break

    return n
