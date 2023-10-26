s = float(input('Qual seu salário atual? '))
p = float(input('Qual a porcentagem de aumento salarial (sem o "%")? '))
ns = s + (s * p / 100)
print('Seu novo salário com {:.2f}% de aumento é de R${:.2f}!'.format(p, ns))
