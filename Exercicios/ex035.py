print('-=' * 5, 'ANALIZADOR DE TRIANGULOS', '-=' * 5)
n1 = float(input('Diga o primeiro lado do trinagulo: '))
n2 = float(input('Diga o segundo lado do triangulo: '))
n3 = float(input('diga o terceiro lado do triangulo: '))
if n2 - n3 < n1 < n2 + n3 and n1 - n3 < n2 < n1 + n3 and n1 - n2 < n3 < n1 + n2:
    print('\033[1;32mEbaa!! Esse triangulo PODE existir!!!!!')
else:
    print('\033[1;31mah... Esse triangulo NÂO PODE existir')
