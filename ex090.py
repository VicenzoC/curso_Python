aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] < 5:
    aluno['Situação'] = 'reprovado'
elif aluno['Média'] < 7:
    aluno['Situação'] = 'recuperação'
else:
    aluno['Situação'] = 'aprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')