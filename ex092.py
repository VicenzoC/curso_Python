import datetime

info =  dict()

info['nome'] = str(input('Nome: '))
datanasc = int(input('Ano de nascimento: '))
info['anos'] = int(datetime.date.today().year) - datanasc
info['cpts'] = str(input('Carteira de trabalho (0 se não tem): '))
if info['cpts'] != '0':
    info['contrato'] = int(input('Ano de contratação: '))
    info['salário'] = float(input('Salário: R$'))
    info['aposentadoria'] = (info['contrato'] + 35) - datanasc
print('\n')
for k, v in info.items():
    print(f'{k} tem o valor {v}')

