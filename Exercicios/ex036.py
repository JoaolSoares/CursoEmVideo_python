casa = float(input('Qual o valora da casa? R$'))
s = float(input('Qual é o seu salario? R$'))
anos = float(input('Em quantos anos a casa será paga? ')) * 12

print('\033[36m=\033[m' * 55)
prest = casa / anos
print('O valora da prestação mensal sairia \033[1;33mR${:.2f}' .format(prest))
print('\033[36m=\033[m' * 55)

if prest <= (s * 30) / 100:
    print('\033[1;32mPARABENS!!!\nO emprestimo bancario foi aprovado!')

else:
    print('\033[1;31mO emprestimo foi recusado...\npela prestaçao mensal exceder 30% do salario do cliente')
