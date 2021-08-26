n1 = int(input('Digite um numero inteiro: '))

print('\033[36m=' * 19)
print("""[ 1 ] -> Binario
[ 2 ] -> Octal
[ 3 ] -> Hexadecimal""")
print('\033[36m=\033[m' * 19)

n2 = int(input('Digite a base que deseja: '))
print('\033[36m=\033[m' * 19)

if n2 == 1:
    print('O numero inteiro {} fica \033[1;32m{}\033[m em Binario' .format(n1, bin(n1)[2:]))

elif n2 == 2:
    print('O numero inteiro {} fica \033[1;32m{}\033[m em Octal' .format(n1, oct(n1)[2:]))

elif n2 == 3:
    print('O numero inteiro {} fica \033[1;32m{}\033[m em Hexadecimal' .format(n1, hex(n1)[2:]))

else:
    print('O numero {} não representa nenhum dialeto...'
          '\nOlhe novamente para a tabela e digite um numero que representa um dialeto' .format(n2))
