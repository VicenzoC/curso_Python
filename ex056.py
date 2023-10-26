somaidade = 0
idademax = 0
nhmax = '' #nome do homem mais velho
contf = 0
for perg in range(1, 5):
    print('{}ª pessoa'.format(perg))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: (M/F) ')).strip().upper()
    somaidade += idade
    if sexo == 'M' and idade > idademax:
        idademax = idade
        nhmax = nome
    if sexo == 'F' and idade < 20:
        contf += 1
midade = somaidade / 4
print('''A média de idade do grupo é {}
O nome do homem mais velho é {}
A quantidade de mulheres menores de 20 anos é {}.'''.format(midade, nhmax.capitalize(), contf))

