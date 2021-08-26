s1 = float(input('Diga o seu salario atual: '))
if s1 >= 1250.00:
    s2 = s1 + ((s1 * 10) / 100)
else:
    s2 = s1 + ((s1 * 15) / 100)
print('O seu salario atual será de \033[7;32mR${:.2f}\033[m' .format(s2))