sal = int(input('Qual o seu salário? '))
if sal > 1250:
    aumento = sal + (sal * 0.1)
    porcentagem = '10%'
else:
    aumento = sal + (sal * 0.15)
    porcentagem = '15%'
print('Seu salário de R${:.2f} foi aumentado em {} e seu salário novo é de R${:.2f}'.format(sal, porcentagem, aumento))

