n1 = int(input('Qual foi sua velocidade: '))
if n1 <= 80:
    print('PARABENS! Por nao ter utrapassado o limite de 80km/h')
else:
    print('ISSO NÃO FOI LEGAL! Você recebera uma multa de R${}' .format((n1 - 80) * 7))