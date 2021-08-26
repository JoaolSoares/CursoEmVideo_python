def leiaint(num):
    while True:
        n1 = input(f'{num} ')
        if n1.isnumeric():
            n1 = int(n1)
            break
        else:
            print('\033[1;31mERRO, Tente novamente...\033[m')
    return n1


print('-=' * 20)
n = leiaint('Digite um numero:')
print(f' =Voce digitou o numero {n}')
print('-=' * 20)
