print('-=' * 5, 'ANALIZADOR DE TRIANGULOS 2.0', '-=' * 5)
n1 = float(input('Diga o primeiro lado do trinagulo: '))
n2 = float(input('Diga o segundo lado do triangulo: '))
n3 = float(input('diga o terceiro lado do triangulo: '))
if n2 - n3 < n1 < n2 + n3 and n1 - n3 < n2 < n1 + n3 and n1 - n2 < n3 < n1 + n2:
    print('\033[1;32mEbaa!! Esse triangulo PODE existir!!!!!')

    if n1 == n2 == n3:
        print('Esse é um triangulo EQUILATERO')

    if n1 == n2 or n1 == n3 or n2 == n3:
        print('Esse é um triangulo ISOCELES')

    if n1 != n2 != n3: # != é igual a 'diferente'
        print('Esse é um triangulo ESCALENO')

else:
    print('\033[1;31mah... Esse triangulo NÂO PODE existir')
